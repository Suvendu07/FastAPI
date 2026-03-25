from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
import os
import time

load_dotenv()


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
        print("connect succesfuly")
        break
    
         
    except Exception as error:
        print("connection failed")
        print(f"error {error}")
        time.sleep(2)
        
        
        

app = FastAPI()


@app.get("/")
def home_page():
    return {
        "message" : "welcome"
    }
    
    
    
@app.get("/retrieve/{id}")
def retreive_by_id(id : int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    data = cursor.fetchone()
    
    if not data:
        raise HTTPException(status_code=404, detail="not found")
    return data