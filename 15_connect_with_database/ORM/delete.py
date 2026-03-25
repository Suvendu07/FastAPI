from fastapi import FastAPI, HTTPException, Depends, Response, status
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
from .database import Base, get_db, engine
from .import models
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import psycopg2
import os
import time



load_dotenv()


app = FastAPI(
    title="delete"
)


Base.metadata.create_all(bind = engine)



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
    
    

@app.delete("/delete{id}")
def delete_data(id : int, db : Session = Depends(get_db)):
    data = db.query(models.Post).filter(models.Post.id == id)
    
    if data.first() == None:
        raise HTTPException(status_code=404, detail="not found")
    
    data.delete(synchronize_session=False)
    db.commit()
    
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)