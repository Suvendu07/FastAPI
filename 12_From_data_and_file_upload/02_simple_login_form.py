from fastapi import FastAPI, Form
from typing import Annotated
from pydantic import EmailStr

app = FastAPI()


@app.get("/")
def home_page():
    return "Welcome"


@app.post("/login")
def login_page(
    name : Annotated[str, Form()],
    password : Annotated[str, Form()]
):
    return {
        "username" : name,
        "message" : "login success"
    }