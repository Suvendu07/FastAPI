"""
The response model is basically use for to avoid sensitive data,

response_model does NOT automatically hide sensitive data.
It only hides fields that are NOT defined in the response model.
"""



# from fastapi import FastAPI
# from pydantic import BaseModel, Field
# from typing import Any

# app = FastAPI(
#     title="Response_model"
# )


# class LoginRequest(BaseModel):
#     username : str
#     password : str
    
# class LoginResponse(BaseModel):
#     user_id : int
#     user_name : str
    
    
# @app.post("/login",response_model=LoginResponse)
# def login(data : LoginRequest):
#     return {
#         "user_id" : 1,
#         "user_name" : data.username,
#         "password" : data.password
#     }



from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


# @app.post("/items/", response_model=Item)
# async def create_item(item: Item) -> Any:
#     return item


@app.post("/items/", response_model=list[Item])
def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]
    
    



# Return the same input data
    
from pydantic import EmailStr


class UserInput(BaseModel):
    name : str
    password : str
    email : EmailStr
    full_name : str | None = None
    

@app.post("/user")
def create_user(data : UserInput):
    return data