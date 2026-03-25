from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/view/{item_id}")
def update_item(item_id : int, item : Item, user : User):
    result = {"item_id":item_id, "item":item, "user":user}
    return result