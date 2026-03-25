from fastapi import FastAPI
from  pydantic import BaseModel, Field


app = FastAPI()

class Suvendu(BaseModel):
    name : str = Field(..., description="enter your name", min_length=0,  max_length=12)
    age : int = Field(..., description="enter your age", min = 0, max = 100)
    salary : float
    location : str


class Khuntia(BaseModel):
    about : str
    suvendu : Suvendu    
    
@app.put("/view")
def get_data(item_id : int, data : Khuntia):
    return {
        "item_id" : item_id,
        "data" : data
    }
    