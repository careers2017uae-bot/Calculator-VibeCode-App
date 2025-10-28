import streamlit as st

st.set_page_config(page_title="Streamlit Calculator", page_icon="🧮", layout="centered")

st.markdown(
    """
    <style>
    div.stButton > button {
        width: 100%;
        height: 70px;
        font-size: 28px;
        font-weight: 800;
        border-radius: 10px;
        background-color: #f0f2f6;
        color: #000;
    }
    div.stButton > button:hover {
        background-color: #dce3f0;
        color: #000;
        border: 2px solid #4b9cd3;
    }
    .display-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        font-size: 36px;
        font-weight: 800;
        text-align: right;
        border: 3px solid #ccc;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🧮 Simple Streamlit Calculator")

# Calculator logic
if "expression" not in st.session_state:
    st.session_state.expression = ""

def press(key):
    if key == "C":
        st.session_state.expression = ""
    elif key == "=":
        try:
            st.session_state.expression = str(eval(st.session_state.expression))
        except:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += key

# Display area
st.markdown(f"<div class='display-box'>{st.session_state.expression}</div>", unsafe_allow_html=True)

# Buttons layout
buttons = [
    ["7", "8", "9", "➗"],
    ["4", "5", "6", "✖️"],
    ["1", "2", "3", "➖"],
    ["0", ".", "=", "➕"],
    ["C"]
]

# 3x3 grid layout (adjusted with last rows centered)
for row in buttons:
    cols = st.columns(4)
    for i, key in enumerate(row):
        if key == "➗":
            label = "➗"
            val = "/"
        elif key == "✖️":
            label = "✖️"
            val = "*"
        elif key == "➖":
            label = "➖"
            val = "-"
        elif key == "➕":
            label = "➕"
            val = "+"
        else:
            label = key
            val = key
        with cols[i]:
            if st.button(label):
                press(val)
