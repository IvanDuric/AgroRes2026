from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="GROCERYsim ABM Presentation",
    page_icon="presentation_html/images/GROCERYsim.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
PRESENTATION_SOURCE = ROOT / "presentation_html"

st.markdown(
    """
    <style>
      html, body, [data-testid="stAppViewContainer"], .stApp {
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        background: #071b24 !important;
      }
      .block-container {
        padding: 0 !important;
        max-width: none !important;
        height: 100vh !important;
      }
      header, footer, [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
        visibility: hidden !important;
        height: 0 !important;
      }
      .stElementContainer, .element-container {
        margin: 0 !important;
        padding: 0 !important;
      }
      iframe[title="st.iframe"] {
        position: fixed !important;
        inset: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        min-height: 100vh !important;
        border: 0 !important;
        display: block !important;
      }
      .presentation-frame {
        position: fixed;
        inset: 0;
        width: 100vw;
        height: 100vh;
        border: 0;
        display: block;
        background: #071b24;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

cache_buster = int((PRESENTATION_SOURCE / "index.html").stat().st_mtime)
st.markdown(
    f"""
    <iframe
      class="presentation-frame"
      src="/app/static/presentation_html/index.html?v={cache_buster}"
      title="GROCERYsim ABM Presentation"
      allow="fullscreen; autoplay"
      allowfullscreen>
    </iframe>
    """,
    unsafe_allow_html=True,
)
