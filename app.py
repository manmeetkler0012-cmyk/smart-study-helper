import streamlit as st

st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator")
st.write("Enter two numbers and click an operation button.")

# --- Input fields ---
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("First number", value=0.0, format="%f")
with col2:
    num2 = st.number_input("Second number", value=0.0, format="%f")

# --- Keep result in session state so it persists between reruns ---
if "result" not in st.session_state:
    st.session_state.result = None
if "expression" not in st.session_state:
    st.session_state.expression = ""

# --- Operation buttons ---
st.write("### Choose an operation")
btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4)

with btn_col1:
    add_clicked = st.button("➕ Add", use_container_width=True)
with btn_col2:
    sub_clicked = st.button("➖ Subtract", use_container_width=True)
with btn_col3:
    mul_clicked = st.button("✖️ Multiply", use_container_width=True)
with btn_col4:
    div_clicked = st.button("➗ Divide", use_container_width=True)

# --- Logic for each button ---
if add_clicked:
    st.session_state.result = num1 + num2
    st.session_state.expression = f"{num1} + {num2}"

elif sub_clicked:
    st.session_state.result = num1 - num2
    st.session_state.expression = f"{num1} - {num2}"

elif mul_clicked:
    st.session_state.result = num1 * num2
    st.session_state.expression = f"{num1} × {num2}"

elif div_clicked:
    if num2 == 0:
        st.session_state.result = None
        st.session_state.expression = f"{num1} ÷ {num2}"
        st.error("❌ Cannot divide by zero!")
    else:
        st.session_state.result = num1 / num2
        st.session_state.expression = f"{num1} ÷ {num2}"

# --- Display result ---
if st.session_state.result is not None:
    st.success(f"**{st.session_state.expression} = {st.session_state.result}**")

st.divider()
st.caption("Built with Streamlit")
