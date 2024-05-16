import requests
import streamlit as st


def get_llama3_response(input_text):
    response=requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']


st.title('Langchain Demo With LLAMA3')
input_text=st.text_input("Write a poem on")

if input_text:
    st.write(get_llama3_response(input_text))
