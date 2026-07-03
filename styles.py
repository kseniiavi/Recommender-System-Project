"""
styles.py
─────────
All CSS for the app lives here, separate from layout logic.
Colors are pulled directly from the mockup:
  - Header/rank-1 card : coral salmon
  - Secondary cards     : light pink
  - Page background     : soft grey
  - Text / progress fill: dark navy
"""

HEADER_BG   = "#EFA695"   # coral salmon (header box, #1 result card)
CARD_BG     = "#FBDCD5"   # light pink (search box, #2 / #3 result cards)
PAGE_BG     = "#F4F2F0"   # soft grey page background
TEXT_DARK   = "#3D3A56"   # dark navy text
BAR_FILL    = "#2D2A45"   # dark navy progress bar fill
BAR_TRACK   = "#F1C9C0"   # lighter pink progress bar track


def get_css() -> str:
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&family=Nunito:wght@400;600;700&display=swap');

    .stApp {{
        background-color: {PAGE_BG};
    }}

    html, body, [class*="css"] {{
        font-family: 'Nunito', sans-serif;
        color: {TEXT_DARK};
    }}

    /* ── Header box ─────────────────────────────────────────────── */
    .st-key-header_box {{
        background-color: {HEADER_BG};
        border-radius: 20px;
        padding: 28px 32px;
        margin-bottom: 20px;
    }}
    .st-key-header_box h1 {{
        font-family: 'Fredoka', sans-serif;
        font-size: 28px;
        font-weight: 600;
        color: {TEXT_DARK};
        margin: 0;
        line-height: 1.35;
    }}

    /* ── Search box ─────────────────────────────────────────────── */
    .st-key-search_box {{
        background-color: {CARD_BG};
        border-radius: 20px;
        padding: 24px 28px 28px 28px;
    }}

    .st-key-search_box input {{
        border-radius: 24px !important;
        border: none !important;
        padding: 14px 20px !important;
        font-size: 15px !important;
        background-color: #FFFFFF !important;
    }}

    /* Arrow submit button */
    .st-key-search_box button[kind="secondaryFormSubmit"],
    .st-key-search_box button[kind="primaryFormSubmit"] {{
        border-radius: 50% !important;
        width: 44px !important;
        height: 44px !important;
        background-color: {TEXT_DARK} !important;
        color: white !important;
        border: none !important;
        font-size: 18px !important;
    }}

    .helper-text {{
        text-align: center;
        font-size: 14px;
        color: {TEXT_DARK};
        opacity: 0.75;
        line-height: 1.7;
        margin-top: 18px;
    }}

    /* ── Suggestion chips ───────────────────────────────────────── */
    .st-key-suggestions button {{
        border-radius: 14px !important;
        background-color: #FFFFFF !important;
        border: 1px solid #E8D4CF !important;
        color: {TEXT_DARK} !important;
        font-size: 13px !important;
        padding: 6px 12px !important;
        text-align: left !important;
    }}

    /* ── Result cards ───────────────────────────────────────────── */
    .result-card {{
        border-radius: 18px;
        padding: 18px 24px;
        margin-bottom: 14px;
    }}
    .result-card.rank-1 {{
        background-color: {HEADER_BG};
    }}
    .result-card.rank-other {{
        background-color: {CARD_BG};
    }}
    .result-title {{
        font-family: 'Fredoka', sans-serif;
        font-weight: 600;
        font-size: 17px;
        margin-bottom: 8px;
    }}
    .result-specialty {{
        font-size: 14px;
        margin-top: 6px;
        opacity: 0.9;
    }}

    /* Custom progress bar */
    .bar-row {{
        display: flex;
        align-items: center;
        gap: 10px;
    }}
    .bar-track {{
        flex-grow: 1;
        height: 10px;
        background-color: {BAR_TRACK};
        border-radius: 6px;
        overflow: hidden;
    }}
    .bar-fill {{
        height: 100%;
        background-color: {BAR_FILL};
        border-radius: 6px;
    }}
    .bar-pct {{
        font-size: 13px;
        font-weight: 600;
        min-width: 42px;
        text-align: right;
    }}

    /* ── Resolution tags ────────────────────────────────────────── */
    .tag {{
        display: inline-block;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        margin: 3px 4px 3px 0;
    }}
    .tag-exact   {{ background-color: #D7EFDD; color: #256B3A; }}
    .tag-synonym {{ background-color: #D7E6EF; color: #21506B; }}
    .tag-fuzzy   {{ background-color: #F5E6C8; color: #7A5B12; }}
    .tag-failed  {{ background-color: #F5D0CC; color: #8B2E25; }}

    /* Back button */
    .st-key-back_btn button {{
        background-color: transparent !important;
        border: 1px solid {TEXT_DARK} !important;
        color: {TEXT_DARK} !important;
        border-radius: 18px !important;
    }}
    </style>
    """
