"""
app_streamlit.py
─────────────────
Web version of the Doctor Specialty Recommender, matching the mockup:
  Screen 1 → landing state:   header + empty search box + helper text
  Screen 2 → typing state:    same layout + live suggestion dropdown
  Screen 3 → results state:   ranked cards with match bars

Run with:  streamlit run app_streamlit.py

Reuses the existing engine — no matching logic is duplicated here:
  resolver.py           → symptom resolution (exact / synonym / fuzzy)
  step4_recommender.py  → cosine similarity ranking
"""

import streamlit as st
from styles import get_css
from resolver import resolve_all, get_all_completion_candidates
from step4_recommender import recommend

st.set_page_config(page_title="Doctor Specialty Recommender", layout="centered")
st.markdown(get_css(), unsafe_allow_html=True)

CANDIDATES = get_all_completion_candidates()

# ── Session state ─────────────────────────────────────────────────────────────
if "stage" not in st.session_state:
    st.session_state.stage = "input"        # "input" | "results"
if "query_text" not in st.session_state:
    st.session_state.query_text = ""
if "resolved" not in st.session_state:
    st.session_state.resolved = []
if "failed" not in st.session_state:
    st.session_state.failed = []
if "results" not in st.session_state:
    st.session_state.results = []
if "gate_message" not in st.session_state:
    st.session_state.gate_message = ""


# ── Helpers ────────────────────────────────────────────────────────────────────
def get_current_word(text: str) -> str:
    """Returns the word being typed after the last comma."""
    if "," in text:
        return text.split(",")[-1].strip()
    return text.strip()


def append_suggestion(candidate: str):
    """Called when a user clicks a suggestion chip — replaces the last (partial) word."""
    text = st.session_state.query_text
    if "," in text:
        parts = [p.strip() for p in text.split(",")[:-1]]
        parts.append(candidate)
        st.session_state.query_text = ", ".join(parts) + ", "
    else:
        st.session_state.query_text = candidate + ", "


def run_recommendation():
    raw_symptoms = [s.strip() for s in st.session_state.query_text.split(",") if s.strip()]
    result = resolve_all(raw_symptoms)
    st.session_state.resolved = result["resolved"]
    st.session_state.failed = result["failed"]

    if len(result["resolved"]) < 3:
        needed = 3 - len(result["resolved"])
        st.session_state.gate_message = (
            f"Only {len(result['resolved'])} symptom(s) recognised. "
            f"Please add at least {needed} more for a reliable result."
        )
        return

    st.session_state.gate_message = ""
    symptom_names = [s for _, s, _ in result["resolved"]]
    st.session_state.results = recommend(symptom_names, top_n=3)
    st.session_state.stage = "results"


def reset():
    st.session_state.stage = "input"
    st.session_state.query_text = ""
    st.session_state.resolved = []
    st.session_state.failed = []
    st.session_state.results = []
    st.session_state.gate_message = ""


# ── SCREEN 1 & 2: input + live suggestions ──────────────────────────────────────
def render_input_screen():
    with st.container(key="header_box"):
        st.markdown(
            "<h1>Let the help reach you faster.<br>Find needed specialist with us!</h1>",
            unsafe_allow_html=True,
        )

    with st.container(key="search_box"):
        with st.form(key="search_form", clear_on_submit=False):
            col1, col2 = st.columns([9, 1])
            with col1:
                query = st.text_input(
                    "symptoms",
                    value=st.session_state.query_text,
                    placeholder="Type your symptoms, separated by commas...",
                    label_visibility="collapsed",
                    key="query_input",
                )
            with col2:
                submitted = st.form_submit_button("→")

            if submitted:
                st.session_state.query_text = query
                run_recommendation()
                st.rerun()

        st.session_state.query_text = query  # keep state in sync as user types

        # ── Live suggestion dropdown ────────────────────────────────────────────
        # Streamlit reruns on every text_input change (Enter/blur), so suggestions
        # update whenever the field is edited. Filters by substring match on the
        # word currently being typed after the last comma.
        current_word = get_current_word(query)
        if len(current_word) >= 2:
            matches = [c for c in CANDIDATES if current_word.lower() in c.lower()][:6]
            if matches:
                with st.container(key="suggestions"):
                    for m in matches:
                        if st.button(m, key=f"sugg_{m}"):
                            append_suggestion(m)
                            st.rerun()

        st.markdown(
            """
            <div class="helper-text">
                Please add at least 3 symptoms for a reliable result.<br>
                More symptoms = better suggestions.<br>
                Type your symptoms separated by commas.<br>
                Example: fever, headache, stiff neck
            </div>
            """,
            unsafe_allow_html=True,
        )

    if st.session_state.gate_message:
        st.warning(st.session_state.gate_message)

    if st.session_state.failed:
        readable_failed = ", ".join(st.session_state.failed)
        st.info(f"Not recognised: {readable_failed} — try rephrasing or check spelling.")


# ── SCREEN 3: results ────────────────────────────────────────────────────────────
def render_results_screen():
    with st.container(key="header_box"):
        st.markdown("<h1>Here's what we found for you</h1>", unsafe_allow_html=True)

    # Show resolved symptoms as tags
    tag_class = {"exact": "tag-exact", "synonym": "tag-synonym", "fuzzy": "tag-fuzzy"}
    tags_html = "".join(
        f'<span class="tag {tag_class.get(method, "tag-exact")}">{symptom.replace("_", " ")}</span>'
        for _, symptom, method in st.session_state.resolved
    )
    st.markdown(tags_html, unsafe_allow_html=True)
    st.write("")

    for r in st.session_state.results:
        rank_class = "rank-1" if r["rank"] == 1 else "rank-other"
        pct = r["similarity"] * 100
        st.markdown(
            f"""
            <div class="result-card {rank_class}">
                <div class="result-title">#{r['rank']} {r['disease']}</div>
                <div class="bar-row">
                    <div class="bar-track">
                        <div class="bar-fill" style="width:{pct}%;"></div>
                    </div>
                    <div class="bar-pct">{pct:.1f}%</div>
                </div>
                <div class="result-specialty">→ See a {r['specialty']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.caption("⚠ This tool is for educational purposes only. Always consult a qualified medical professional.")

    with st.container(key="back_btn"):
        if st.button("← Search again"):
            reset()
            st.rerun()


# ── Router ────────────────────────────────────────────────────────────────────
if st.session_state.stage == "input":
    render_input_screen()
else:
    render_results_screen()
