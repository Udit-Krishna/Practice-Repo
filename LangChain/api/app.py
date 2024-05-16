from fastapi import FastAPI
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceEndpoint
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('HUGGINGFACEHUB_API_KEY')
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"
)

repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"
llm = HuggingFaceEndpoint(
    repo_id=repo_id, temperature=0.6, token=api_key
)

prompt = PromptTemplate(input_variables=["topic"],
        template="""
        Write a poem about {topic}.  
    """
)


add_routes(
    app,
    prompt|llm,
    path="/poem"
)



if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)