import streamlit as st

st.title("Simple Streamlit Test App")

name = st.text_input("Enter your name:")
number = st.slider("Pick a number", 1, 100, 50)

if st.button("Submit"):
    st.write(f"Hello, **{name}**! 👋")
    st.write(f"You chose the number **{number}**.")
