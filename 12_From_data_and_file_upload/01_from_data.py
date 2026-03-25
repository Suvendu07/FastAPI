"""Instead of using a Pydantic model, we use Form() when data is sent from an HTML form (like login or register pages).
The client sends data in form format, and FastAPI reads it using Form().
The response is still JSON unless we explicitly return HTML.


Use Form() when:

HTML form submission

Login / Register pages

File uploads

Traditional server-rendered apps

"""


from fastapi import FastAPI, Form
from pydantic import BaseModel, Field


app = FastAPI(
    title="Form Data"
)


# without form
class Data(BaseModel):
    name : str = Field(..., description="enter the name")
    age : int = Field(..., description="enter your age")
    
    
@app.put("/view{item_id}")
def update_data(item_id:int,data : Data):
    return {
        "item_id" : item_id,
        "data" : data
    }
    

# with Form

@app.put("/update")
def update_item(item_name:str = Form(), name : str = Form()):
    return {
        "item_name" : item_name,
        "name" : name
    }