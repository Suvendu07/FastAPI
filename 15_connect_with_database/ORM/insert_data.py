from fastapi import FastAPI, HTTPException, Depends
from .database import get_db, Base, engine
from .import models
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import time 
import os
import psycopg2
from pydantic import BaseModel



load_dotenv()

models.Base.metadata.create_all(bind = engine)



app = FastAPI(
    title="insert_data_orm"
)


class Post(BaseModel):
    title : str
    content : str
    published : bool


while True:
    try:
        conn = psycopg2.connect(
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME"),
            cursor_factory=RealDictCursor
        )
        
        cursor = conn.cursor()
        print("database connected successfully")
        break
    
    
    except Exception as error:
        print("failed to connect")
        print(f"error: {error}")
        time.sleep(2)
        
        
@app.post("/create")
def insert_data(post : Post, db : Session = Depends(get_db)):
    
    new_post = models.Post(title = post.title, content = post.content, published = post.published)
    
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post



"""in this table we have just 5 colums so that we write title = post.title like this what if in our table lot's of and in write this way take lot's of time so to solve this type of problem use python unpack dict methos"""


@app.post("/creates")
def create_posts(post : Post, db : Session = Depends(get_db)):
    
    new_post = models.Post(
        **post.dict()
    )
    
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    
    return new_post