import streamlit as st

st.set_page_config(
    page_title="Smart Study Helper",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Smart Study Helper")

st.write("""
## Welcome!

Choose a tool from the sidebar.

### Available Tools
- 📚 Study Helper
- 🧙 Wizard Calculator
""")

st.success("👈 Select a page from the sidebar.")
