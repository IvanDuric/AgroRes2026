from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="GROCERYsim ABM Presentation",
    page_icon="presentation_html/images/GROCERYsim.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
PRESENTATION_SOURCE = ROOT / "presentation_html"
RAW_ASSET_BASE = (
    "https://raw.githubusercontent.com/IvanDuric/AgroRes2026/main/"
    "SecureFood_presentation_streamlit/presentation_html"
)

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
      iframe {
        position: fixed !important;
        inset: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        min-height: 100vh !important;
        border: 0 !important;
        display: block !important;
        background: #071b24 !important;
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

presentation_html = (PRESENTATION_SOURCE / "index.html").read_text(encoding="utf-8")
for asset_dir in ("images", "videos", "scenario_results"):
    presentation_html = presentation_html.replace(
        f'src="{asset_dir}/',
        f'src="{RAW_ASSET_BASE}/{asset_dir}/',
    )
    presentation_html = presentation_html.replace(
        f"src='{asset_dir}/",
        f"src='{RAW_ASSET_BASE}/{asset_dir}/",
    )

components.html(presentation_html, height=1000, scrolling=False)
