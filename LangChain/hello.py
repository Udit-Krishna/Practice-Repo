from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import HuggingFaceEndpoint
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('HUGGINGFACEHUB_API_KEY')
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = PromptTemplate(input_variables=["question"],
        template="""
        You are a helpful assistant. Please respond only to the user question.
        Question: {question}.  
    """
)

st.title("LangChain Demo with Llama3")

input_text = st.text_input("Enter your text here")

repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"
llm = HuggingFaceEndpoint(
    repo_id=repo_id, temperature=0.6, token=api_key
)

output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
