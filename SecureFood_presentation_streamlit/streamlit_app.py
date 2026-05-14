from pathlib import Path
import base64
import mimetypes
import re

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="GROCERYsim ABM Presentation",
    page_icon="presentation_html/images/GROCERYsim.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
HTML_PATH = ROOT / "presentation_html" / "index.html"
ASSET_PATTERN = re.compile(r'(src=")(?!https?://|data:|#)([^"]+)(")')


def file_to_data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


def inline_local_assets(html: str) -> str:
    base = HTML_PATH.parent

    def replace(match: re.Match[str]) -> str:
        prefix, src, suffix = match.groups()
        asset_path = (base / src).resolve()
        if not asset_path.exists():
            return match.group(0)
        return f"{prefix}{file_to_data_uri(asset_path)}{suffix}"

    return ASSET_PATTERN.sub(replace, html)


html = inline_local_assets(HTML_PATH.read_text(encoding="utf-8"))

st.markdown(
    """
    <style>
      .block-container { padding: 0 !important; max-width: none !important; }
      header, footer { visibility: hidden; height: 0; }
      iframe { display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(html, height=920, scrolling=False)
