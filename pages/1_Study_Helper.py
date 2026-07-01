import streamlit as st
import random

st.set_page_config(page_title="Wizard's Magic Calculator", page_icon="🧙", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #1a0033, #330066, #4d0099);
    }
    h1, h2, h3, p, label, .stMarkdown {
        color: #f2e6ff !important;
    }
    div.stButton > button {
        height: 65px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 20px;
        border: 2px solid #ffcc00;
        background: linear-gradient(135deg, #6600cc, #9933ff);
        color: white;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #ff33cc, #ff6699);
        border: 2px solid white;
    }
    div[data-testid="stNumberInput"] input {
        background-color: #2d004d;
        color: #ffcc00;
        font-weight: bold;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align:center;'>🧙‍♂️ Wizard's Magic Calculator 🔮</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Cast a spell on two numbers and watch the magic happen ✨</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("🌙 First magic number", value=0.0, format="%f")
with col2:
    num2 = st.number_input("⭐ Second magic number", value=0.0, format="%f")

if "result" not in st.session_state:
    st.session_state.result = None
if "expression" not in st.session_state:
    st.session_state.expression = ""

spell_messages = [
    "Abracadabra! 🪄",
    "Poof! Magic complete! ✨",
    "The spirits have spoken! 👻",
    "Ta-da! ✨🎩",
    "The crystal ball reveals... 🔮",
]

st.markdown("### 🪄 Choose your spell")
b1, b2, b3, b4 = st.columns(4)
add_clicked = b1.button("🔥 Combine", use_container_width=True)
sub_clicked = b2.button("❄️ Banish", use_container_width=True)
mul_clicked = b3.button("⚡ Multiply Charm", use_container_width=True)
div_clicked = b4.button("💧 Split Spell", use_container_width=True)

def show_result(answer, symbol):
    st.session_state.result = answer
    st.session_state.expression = f"{num1} {symbol} {num2}"

if add_clicked:
    show_result(num1 + num2, "+")
elif sub_clicked:
    show_result(num1 - num2, "-")
elif mul_clicked:
    show_result(num1 * num2, "×")
elif div_clicked:
    if num2 == 0:
        st.session_state.result = None
        st.error("🚫 Even wizards can't divide by zero!")
    else:
        show_result(num1 / num2, "÷")

if st.session_state.result is not None:
    st.markdown(f"## {random.choice(spell_messages)}")
    st.markdown(
        f"<h2 style='text-align:center; color:#ffcc00;'>{st.session_state.expression} = {st.session_state.result}</h2>",
        unsafe_allow_html=True,
    )

    # Playful reactions based on the result
    if st.session_state.result == 0:
        st.snow()
        st.write("🌨️ A number of pure nothingness... how mysterious.")
    elif st.session_state.result > 100:
        st.balloons()
        st.write("🎈 WHOA! That's a HUGE number! The kingdom celebrates!")
    elif st.session_state.result < 0:
        st.write("🦇 A negative number... the dark side of math!")
    else:
        st.write("✨ A fine and balanced result, young wizard.")

st.divider()
st.markdown("<p style='text-align:center; font-size:13px;'>Made with 🪄 and Streamlit</p>", unsafe_allow_html=True)
