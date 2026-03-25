from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Path


app = FastAPI()

class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None
    
@app.put("/item{item_id}")
def update_item(
    item_id : Annotated[int, Path(title="The Id of the item to get", ge=0,le=1000)],
    q : str | None = None,
    item : Item | None = None
):
    result = {"item_id":item_id}
    if q:
        result.update({"q":q})
    if item:
        result.update({"item":item})
        
    return result