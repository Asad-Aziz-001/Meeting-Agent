import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Meeting-to-Action Pipeline",
    page_icon="⚡",
    layout="wide"
)

# Read the HTML file
with open("index.html", "r") as f:
    html_content = f.read()

# Render full HTML app
components.html(html_content, height=900, scrolling=True)
