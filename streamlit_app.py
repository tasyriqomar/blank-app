import streamlit as st

st.write("Hello World")
x = st.text_input("Favourite Movies?")
st.write(f"Your favourite movie is: {x}")