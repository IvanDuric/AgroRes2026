from pathlib import Path
import shutil

import streamlit as st


st.set_page_config(
    page_title="GROCERYsim ABM Presentation",
    page_icon="presentation_html/images/GROCERYsim.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
PRESENTATION_SOURCE = ROOT / "presentation_html"
STATIC_PRESENTATION = ROOT / "static" / "presentation_html"


def sync_static_presentation() -> None:
    """Mirror the presentation into Streamlit's static directory."""
    STATIC_PRESENTATION.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(PRESENTATION_SOURCE, STATIC_PRESENTATION, dirs_exist_ok=True)


sync_static_presentation()

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
    </style>
    """,
    unsafe_allow_html=True,
)

cache_buster = int((PRESENTATION_SOURCE / "index.html").stat().st_mtime)
st.iframe(
    f"/app/static/presentation_html/index.html?v={cache_buster}",
    width="stretch",
    height="stretch",
)
