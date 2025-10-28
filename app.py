import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Realistic Calculator", layout="centered")
st.markdown("<h1 style='text-align:center;'>🧮 Streamlit Calculator</h1>", unsafe_allow_html=True)

# --- Initialize State ---
if "expression" not in st.session_state:
    st.session_state.expression = ""

# --- CSS Styling for Realistic Look ---
st.markdown("""
    <style>
        div.stTextInput > div > input {
            font-size: 28px !important;
            text-align: right;
            border: 2px solid #4CAF50;
            border-radius: 10px;
            background-color: #f7f7f7;
            color: black;
            height: 60px;
        }
        div.stButton > button {
            height: 60px;
            width: 100%;
            font-size: 22px !important;
            font-weight: bold;
            border-radius: 10px;
            margin: 2px;
            background-color: #e0e0e0;
            color: black;
            border: none;
        }
        div.stButton > button:hover {
            background-color: #4CAF50;
            color: white;
            border: none;
        }
        hr {
            margin-top: 30px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Display Screen ---
display = st.text_input("", st.session_state.expression, key="display", label_visibility="collapsed")

# --- Button Logic ---
def press(btn):
    if btn == "C":
        st.session_state.expression = ""
    elif btn == "=":
        try:
            expression = st.session_state.expression.replace("×", "*").replace("÷", "/")
            st.session_state.expression = str(eval(expression))
        except Exception:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += btn

# --- Button Layout (like a real calculator) ---
buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
]

# --- Create Calculator Grid ---
for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        if cols[i].button(btn, use_container_width=True):
            press(btn)

# --- Last Row for Clear and Equal Buttons ---
colC, colEq = st.columns([1, 1])
if colC.button("C", use_container_width=True):
    press("C")
if colEq.button("=", use_container_width=True):
    press("=")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Made with ❤️ using Streamlit — A Realistic Calculator Experience")
