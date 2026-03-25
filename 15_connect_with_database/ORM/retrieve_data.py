from typing import Optional
from fastapi import FastAPI, HTTPException, Response, status, Depends
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
import time
from .database import get_db, engine, Base
from psycopg2.extras import RealDictCursor
# from . import models
from .models import Post
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv
import time


load_dotenv()

# models.Base.metadata.create_all(bind = engine)
Base.metadata.create_all(bind = engine)


app = FastAPI(
    title="ORM"
)



while True:
    try:
           conn = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        user = os.getenv("DB_USER"),
        database = os.getenv("DB_NAME"),
        password = os.getenv("DB_PASSWORD"),
        cursor_factory=RealDictCursor
    )
           cursor = conn.cursor()
           print("database connected successfully")
           break
       
       
    except Exception as error:
        print("failed connection")
        print(f"error: {error}")
        time.sleep(2)
        
        
        
        
@app.get("/")
def home_page():
    return {
        "message" : "Hello Suvendu"
    }
    
    

"""GET ALL"""
@app.get("/getalldata")
def get_data(db : Session = Depends(get_db)):
    
    # data = db.query(models.Post).all()
    data = db.query(Post).all()
    
    return data


