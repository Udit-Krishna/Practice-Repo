import uvicorn
from fastapi import FastAPI
from IrisFlower import IrisFlower
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)


@app.get('/')
def index():
    return {
        'message' : 'Hello, World!'
    }

@app.get('/welcome')
def get_name(name:str):
    return {
        'Welcome to my page' : f'{name}'
    }

@app.post('/predict')
def predict_species(data: IrisFlower):
    data = data.model_dump()
    print(data)
    sepal_length = data["sepal_length"]
    sepal_width = data["sepal_width"]
    petal_length = data["petal_length"]
    petal_width = data["petal_width"]
    [sepal_length,sepal_width,petal_length,petal_width]
    prediction = classifier.predict([[sepal_length,sepal_width,petal_length,petal_width]])
    print(prediction)
    prediction = {
        "Predicted Species" : f"{prediction[0]}"
    }
    return prediction

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
    #uvicorn main:app --reload