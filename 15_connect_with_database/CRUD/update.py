from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import psycopg2
import os
import time




load_dotenv()


while True:
    try:
        conn = psycopg2.connect(
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME"),
            cursor_factory = RealDictCursor
        )
        
        cursor = conn.cursor()
        print("database connected sucessfully")
        break
    
    
    except Exception as error:
        print("failed connect")
        print(f"error: {error}")
        time.sleep(2)


app = FastAPI()


class Post(BaseModel):
    title : str
    content : str
    published : bool
    
    
    
@app.get("/")
def home_page():
    return {
        "message" : "welcome"
    }
    
    
@app.put("/update/{id}")
def update_data(id : int, post : Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s""",(post.title, post.content, post.published, str(id)))
    
    
    conn.commit()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="id not found")
    return {
        "message" : "updated successfuly"
    }