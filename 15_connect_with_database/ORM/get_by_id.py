from .database import get_db, Base, engine
from . import models
from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor
import psycopg2
import time
import os
from sqlalchemy.orm import Session


load_dotenv()



Base.metadata.create_all(bind = engine)


app = FastAPI(
    title="get_by_id"
)

    
while True:
    try:
        conn = psycopg2.connect(
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            database = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            cursor_factory=RealDictCursor
        )
        
        cursor = conn.cursor()
        print("db connect successfully")
        break
    
        
    except Exception as error:
        print("failed to connect")  
        print(f"error {error}")
        time.sleep(2)
        
        
@app.get("/")
def home_page():
    return {
        "message" : "welcome"
    }
    
    

@app.get("/get_by_id/{id}")
def get_by_id(id : int, db : Session = Depends(get_db)):
    
    data = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not data:
        raise HTTPException(status_code=404, detail="id not found")
    return data