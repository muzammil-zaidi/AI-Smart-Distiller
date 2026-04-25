import streamlit as st
import os

_FA_CSS = None

def get_fa_css():
    global _FA_CSS
    if _FA_CSS is None:
        css_path = os.path.join(os.path.dirname(__file__), "static", "fontawesome", "css", "fa-embedded.css")
        with open(css_path, "r") as f:
            _FA_CSS = f.read()
    return _FA_CSS

def inject_fa():
    css = get_fa_css()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def fa(icon_class, extra_style=""):
    """Return an FA icon span. icon_class e.g. 'fa-brain' """
    style = f' style="{extra_style}"' if extra_style else ""
    return f'<i class="fas {icon_class}"{style}></i>'
