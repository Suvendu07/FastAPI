from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI()


class BaseUser(BaseModel):
    name: str
    email : EmailStr
    
class UserIn(BaseUser):
    password : str
    

@app.post("/login")
async def create_user(user : UserIn) -> BaseUser:
    return user


