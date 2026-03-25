from fastapi import FastAPI, File, UploadFile
from typing import Annotated


app = FastAPI(
    title="multiple file upload"
)


@app.post("/file")
def file(file : Annotated[list[bytes], File()]):
    return {
        "file_len" : list[len(file for files in file)]
    }
    

@app.post("/uploadfile")
def upload_file(file : list[UploadFile]):
    
        return {"filenames": [file.filename for files in file]}   