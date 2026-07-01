import streamlit as st

st.set_page_config(
    page_title="Smart Study Helper",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📚 Smart Study Helper")

st.sidebar.title("📚 Navigation")
st.sidebar.success("Choose a tool below")

st.write("""
## Welcome!

Select a page from the sidebar.

### Available Tools
- 📚 Study Helper
- 🧙 Wizard Calculator
""")

st.success("👈 Open the sidebar and choose a page.")
