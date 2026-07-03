import streamlit as st

# Import the exact components from your backend logic files
from resolver import resolve_all, get_all_completion_candidates
from step4_recommender import recommend

# ==========================================
# 1. FIGMA DESIGN STYLING (Custom CSS)
# ==========================================
st.set_page_config(page_title="Doctor Specialty Recommender", layout="centered")

st.markdown("""
    <style>
    /* Background setup */
    .stApp {
        background-color: #F4F4F6;
    }
    
    /* Header Box */
    .header-box {
        background-color: #EFA79A;
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.02);
    }
    .header-title {
        color: #4A2E2B;
        font-family: 'Courier New', Courier, monospace;
        font-size: 26px;
        font-weight: bold;
        margin: 0;
    }

    /* Input Card Container */
    .input-card {
        background-color: #FCEBE7;
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 20px;
        position: relative;
    }
    .instruction-text {
        color: #614643;
        font-family: 'Courier New', Courier, monospace;
        font-size: 14px;
        line-height: 1.6;
        text-align: left;
        margin-top: 15px;
    }

    /* Info Banner (Dark bottom overlay) */
    .info-banner {
        background-color: #727288;
        color: #FFFFFF;
        border-radius: 16px;
        padding: 15px 20px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 13px;
        text-align: center;
        line-height: 1.5;
        margin-top: 15px;
        margin-bottom: 25px;
    }

    /* Results Recommendation Cards */
    .result-card {
        background-color: #FCEBE7;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 15px;
        font-family: 'Courier New', Courier, monospace;
        color: #4A2E2B;
    }
    .result-rank {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .result-specialty {
        font-size: 16px;
        margin-top: 5px;
        font-weight: bold;
    }

    /* Figma Bar Progress Layout */
    .progress-container {
        display: flex;
        align-items: center;
        margin: 8px 0;
    }
    .progress-label {
        width: 60px;
        font-size: 14px;
    }
    .progress-bg-bar {
        background-color: #555568;
        border-radius: 4px;
        flex-grow: 1;
        height: 14px;
        margin: 0 10px;
        position: relative;
        overflow: hidden;
    }
    .progress-fill-bar {
        background-color: #1F1F2E;
        height: 100%;
        border-radius: 4px 0 0 4px;
    }
    .progress-percentage {
        width: 65px;
        text-align: right;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# State initialization for session memory handling
if "page" not in st.session_state:
    st.session_state.page = "search"  # Can be 'search' or 'analysis'
if "user_selected_symptoms" not in st.session_state:
    st.session_state.user_selected_symptoms = []

# ==========================================
# PAGE 1: SEARCH & ENTRY SCREEN
# ==========================================
if st.session_state.page == "search":
    
    # Application Header
    st.markdown("""
        <div class="header-box">
            <p class="header-title">Let the help reach you faster.<br>Find needed specialist with us!</p>
        </div>
    """, unsafe_allow_html=True)

    candidates = get_all_completion_candidates()

    st.markdown('<div class="input-card">', unsafe_allow_html=True)

    # Multi-select input panel.
    # Pressing Enter on a typed term automatically locks it into the value list.
    selected_symptoms = st.multiselect(
        label="Search and select symptoms",
        options=candidates,
        default=st.session_state.user_selected_symptoms,
        placeholder="Type to search symptoms...",
        label_visibility="collapsed"
    )
    # Sync structural updates instantly into session memory
    st.session_state.user_selected_symptoms = selected_symptoms

    # Instructions text framework
    st.markdown("""
        <div class="instruction-text">
            Please add at least 3 symptoms for a reliable result.<br>
            More symptoms = better suggestions.<br>
            Type your symptoms and press Enter to confirm them.<br>
            <strong>Example:</strong> fever, headache, stiff neck
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Action navigation center layout
    st.write("")
    action_cols = st.columns([2, 1, 2])
    with action_cols[1]:
        # Lock analysis route execution gates until requirement specifications are satisfied
        if len(selected_symptoms) >= 3:
            if st.button("Analyze Symptoms", use_container_width=True):
                st.session_state.page = "analysis"
                st.rerun()
        else:
            st.button("Analyze Symptoms", disabled=True, use_container_width=True, help="Select at least 3 symptoms first.")

    # Educational informational footer panel
    st.markdown("""
        <div class="info-banner">
            This tool uses content-based filtering and cosine similarity to recommend<br>
            medical specialists based on your symptoms.<br>
            This tool is for educational purposes only.<br>
            Always consult a qualified medical professional for medical advice.
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# PAGE 2: ANALYSIS & RECOMMENDATIONS SCREEN
# ==========================================
elif st.session_state.page == "analysis":
    
    # Navigation utilities area
    if st.button("← Back to search"):
        # COMPLETELY RENEW SESSION STATE: Clear the page layout and reset symptoms list
        st.session_state.user_selected_symptoms = []
        st.session_state.page = "search"
        st.rerun()
        
    st.write("### Diagnostics & System Recommendations")
    
    # Unpack system inputs straight from user selection data structures
    result = resolve_all(st.session_state.user_selected_symptoms)
    resolved = result["resolved"]
    symptom_names = [s for _, s, _ in resolved]
    
    # Compute system algorithmic model outputs
    recommendations = recommend(symptom_names, top_n=3)
    
    # Loop over live output dictionary matching custom metric graphs 
    for r in recommendations:
        bar_width = int(r["similarity"] * 100)
        
        st.markdown(f"""
            <div class="result-card">
                <div class="result-rank">#{r['rank']} {r['disease']}</div>
                <div class="progress-container">
                    <div class="progress-label">Match</div>
                    <div class="progress-bg-bar">
                        <div class="progress-fill-bar" style="width: {bar_width}%;"></div>
                    </div>
                    <div class="progress-percentage">{r['confidence']}</div>
                </div>
                <div class="result-specialty">→ See a {r['specialty']}</div>
            </div>
        """, unsafe_allow_html=True)