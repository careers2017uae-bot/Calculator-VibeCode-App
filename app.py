import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Realistic Calculator", layout="centered")
st.markdown("<h1 style='text-align:center;'>🧮 Vibe-Coded Calculator</h1>", unsafe_allow_html=True)

# --- Initialize State ---
if "expression" not in st.session_state:
    st.session_state.expression = ""

# --- Custom Styling for Realistic Look ---
st.markdown("""
    <style>
        div[data-testid="stTextArea"] textarea {
            font-size: 28px !important;
            text-align: right;
            height: 70px !important;
            border-radius: 10px;
            border: 2px solid #4CAF50;
            background-color: #f7f7f7;
            color: black;
        }
        div.stButton > button {
            height: 65px;
            width: 100%;
            font-size: 60px !important;
            font-weight: bold;
            border-radius: 10px;
            margin: 3px;
            background-color: #e0e0e0;
            color: black;
            border: none;
            box-shadow: 1px 1px 2px #aaa;
        }
        div.stButton > button:hover {
            background-color: #4CAF50;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# --- Display Box ---
st.text_area("Display", value=st.session_state.expression, height=70, label_visibility="collapsed")

# --- Function to handle button click ---
def press(btn):
    if btn == "C":
        st.session_state.expression = ""
    elif btn == "=":
        try:
            exp = st.session_state.expression.replace("×", "*").replace("÷", "/")
            st.session_state.expression = str(eval(exp))
        except Exception:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += btn
    st.rerun()

# --- Calculator Layout (with proper escaping) ---
buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
]

# --- Create Grid Buttons ---
for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        label = btn.replace("+", "➕").replace("-", "➖")
        if cols[i].button(label, use_container_width=True):
            press(btn)

# --- Bottom Row for Clear and Equal ---
colC, colEq = st.columns(2)
if colC.button("C", use_container_width=True):
    press("C")
if colEq.button("=", use_container_width=True):
    press("=")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Made with ❤️ using Streamlit — Realistic Working Calculator by Engr. Bilal")
