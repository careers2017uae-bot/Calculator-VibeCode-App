import streamlit as st

# --- App Title ---
st.set_page_config(page_title="Simple Calculator", layout="centered")
st.title("🧮 Simple Streamlit Calculator")

st.markdown("### Enter numbers and choose an operation:")

# --- Input Section ---
col1, col2, col3 = st.columns(3)

with col1:
    num1 = st.number_input("First Number", step=1.0, key="num1")

with col2:
    operation = st.selectbox(
        "Operation",
        ["+", "-", "×", "÷", "%"],
        index=0,
        key="operation"
    )

with col3:
    num2 = st.number_input("Second Number", step=1.0, key="num2")

# --- 3x3 Grid Buttons for Digits ---
st.markdown("### Keypad (for quick entry)")

grid_cols = st.columns(3)
buttons = [
    ("1", "2", "3"),
    ("4", "5", "6"),
    ("7", "8", "9")
]

for row in buttons:
    cols = st.columns(3)
    for i, btn in enumerate(row):
        if cols[i].button(btn):
            st.session_state.num1 = st.session_state.num1 * 10 + int(btn)

# --- Perform Calculation ---
if st.button("Calculate Result"):
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "×":
            result = num1 * num2
        elif operation == "÷":
            if num2 == 0:
                st.error("❌ Cannot divide by zero!")
                st.stop()
            result = num1 / num2
        elif operation == "%":
            result = num1 % num2
        st.success(f"✅ Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Made with ❤️ using Streamlit")
