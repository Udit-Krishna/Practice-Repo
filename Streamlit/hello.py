import streamlit as st

st.write("Hello World")
movie = st.text_input("What's your favorite movie?")
st.write(f"Your favorite movie is {movie}")
st.link_button("Calculator", "/Calculator")