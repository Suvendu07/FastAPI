from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os
import time


load_dotenv()


app = FastAPI(
    title="CRUD operation"
)


class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    
    
while True:
    try:
        conn = psycopg2.connect(
            host = os.getenv("DB_HOST"),
            database = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            port = os.getenv("DB_PORT"),
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("database connct succesful")
        break
        
    except Exception as error:
        print("connection failed")
        print(f"error {error}")
        time.sleep(2)
        
        
        
@app.get("/")
def home_page():
    return {
        "message" : "hello world"
    }
    
    

@app.post("/insert")
def insert_data(data : Post):
    cursor.execute("""INSERT INTO posts(title, content, published) VALUES (%s, %s, %s) RETURNING *""",(data.title, data.content, data.published))
    new_data = cursor.fetchone()
    conn.commit()
    return {
        "data" : new_data
    }