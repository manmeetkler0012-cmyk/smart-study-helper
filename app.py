import streamlit as st

st.set_page_config(
    page_title="Smart Study Helper",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("📚 Navigation")
st.sidebar.page_link("pages/1_Study_Helper.py", label="Study Helper")
st.sidebar.page_link("pages/2_Wizard_Calculator.py", label="Wizard Calculator")

st.title("📚 Smart Study Helper")

st.write("""
## Welcome!

Choose a tool from the sidebar.
""")
