import streamlit as st
import time
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader



from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    temperature=0.6,
    do_sample=False,
)


st.title("Chat with your PDF using Llama 3")
st.title("")

prompt = PromptTemplate.from_template(
    """
Answer the questions based on the provided context only.
Please provide the most accurate response based only on the question like a human.
The answer should always be always very brief without unnecessary words.
Context: {context}
Question: {input}
Answer:
"""
)


def vector_embedding():
    st.session_state.embeddings=HuggingFaceEndpointEmbeddings(
                                    model= "sentence-transformers/all-MiniLM-L12-v2",
                                )
    st.session_state.loader=PyPDFLoader("file.pdf")
    st.session_state.docs=st.session_state.loader.load()
    st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs)
    st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)

st.sidebar.header("Upload your PDF file here")
uploaded_file = st.sidebar.file_uploader("Upload .pdf here", type=['pdf'], label_visibility="hidden")

if not uploaded_file:
    st.warning("Upload a file to start chatting")

if uploaded_file:
    bytes_data = uploaded_file.getvalue()
    with open("file.pdf", 'wb') as f: 
        f.write(bytes_data)
    vector_embedding()
    st.sidebar.success("Vector Store DB Is Ready")


    prompt1=st.text_input("Enter Your Question From Documents")

    if prompt1:
        document_chain=create_stuff_documents_chain(llm,prompt)
        retriever=st.session_state.vectors.as_retriever()
        retrieval_chain=create_retrieval_chain(retriever,document_chain)
        start=time.process_time()
        response=retrieval_chain.invoke({'input':prompt1})
        print("Response time :",time.process_time()-start)
        st.write(response['answer'])

        with st.expander("Document Similarity Search"):
            for i, doc in enumerate(response["context"]):
                st.write(doc.page_content)
                st.write("--------------------------------")