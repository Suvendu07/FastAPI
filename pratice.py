from fastapi import FastAPI, HTTPException
import json

app = FastAPI()


def load_data():
    with open("patients.json","r") as f:
        data = json.load(f)
    return data


@app.get("/")
def view():
    return "hello"

@app.get("/view")
def patient():
    data = load_data()
    
    return data