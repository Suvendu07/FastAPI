"""FastAPI supports file uploads using File() for small files loaded as bytes and UploadFile for efficient streaming of large files via multipart form-data.



When should YOU use which?
Use bytes + File() when:

File is very small

Just checking size or hash

Use UploadFile when:

File upload feature

Images, PDFs, videos

ML datasets

Production APIs"""

from fastapi import FastAPI, File, UploadFile
from typing import Annotated

app = FastAPI(
    title= "file upload"
)

@app.post("/file")
def file(file : Annotated[bytes, File()]):
    return {
        "file_len" : len(file)
    }
    
    
@app.post("/uploadfile")
def uploadfile(file : UploadFile):
    return {
        "file_name" : file.filename
    }
    
    
    
    
    


@app.post("/files/")
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    return {"filename": file.filename}