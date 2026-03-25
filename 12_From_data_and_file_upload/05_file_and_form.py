from fastapi import FastAPI, File, UploadFile, Form
from pydantic import Field
from typing import Annotated


app = FastAPI(
    title="form and filed"
)


@app.post("/login")
def create_file(filea : Annotated[bytes, File()], fileb : Annotated[UploadFile, File()], token : Annotated[str, Form()]):
    
    return {
        "file_a" : len(filea),
        "file_b" : fileb.content_type,
        "token" : token
    }