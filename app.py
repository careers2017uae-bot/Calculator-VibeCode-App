import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Realistic Calculator", layout="centered")
st.markdown("<h1 style='text-align:center;'>🧮 Streamlit Calculator</h1>", unsafe_allow_html=True)

# --- Initialize State ---
if "expression" not in st.session_state:
    st.session_state.expression = ""

# --- Symbol Mapping ---
symbol_map = {
    "0": "⓪", "1": "①", "2": "②", "3": "③", "4": "④",
    "5": "⑤", "6": "⑥", "7": "⑦", "8": "⑧", "9": "⑨",
    ".": "⬤", "+": "➕", "-": "➖", "*": "✖️", "/": "➗",
    "%": "％", "C": "🔄", "=": "🟰"
}

# --- Custom Styling ---
st.markdown("""
    <style>
        div[data-testid="stTextArea"] textarea {
            font-size: 30px !important;
            text-align: right;
            height: 80px !important;
            border-radius: 12px;
            border: 3px solid #4CAF50;
            background-color: #f7f7f7;
            color: black;
        }
        div.stButton > button {
            height: 70px;
            width: 100%;
            font-size: 28px !important;
            font-weight: bold;
            border-radius: 12px;
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
st.text_area("Display", value=st.session_state.expression, height=80, label_visibility="collapsed")

# --- Button Press Logic ---
def press(btn):
    if btn == "C":
        st.session_state.expression = ""
    elif btn == "=":
        try:
            exp = st.session_state.expression.replace("×", "*").replace("✖️", "*").replace("÷", "/").replace("➗", "/")
            st.session_state.expression = str(eval(exp))
        except Exception:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += btn
    st.rerun()

# --- Button Layout ---
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
]

# --- Create Grid Buttons ---
for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        label = symbol_map.get(btn, btn)
        if cols[i].button(label, use_container_width=True):
            press(btn)

# --- Bottom Row (Clear + Equal) ---
colC, colEq = st.columns(2)
if colC.button(symbol_map["C"], use_container_width=True):
    press("C")
if colEq.button(symbol_map["="], use_container_width=True):
    press("=")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Made with ❤️ using Streamlit — Emoji-Style Realistic Calculator")
