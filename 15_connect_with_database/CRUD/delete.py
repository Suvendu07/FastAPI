from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
import psycopg2
import time
from psycopg2.extras import RealDictCursor



load_dotenv()


while True:
    try:
        conn = psycopg2.connect(
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            password = os.getenv("DB_PASSWORD"),
            user = os.getenv("DB_USER"),
            database = os.getenv("DB_NAME"),
            cursor_factory=RealDictCursor
        )
        
        cursor = conn.cursor()
        print("database connect successfuly")

        break
    
    
    except Exception as error:
        print("failed connection")
        print(f"error {error}")
        time.sleep(2)




app = FastAPI()



@app.get("/")
def home_page():
    return {
        "message" : "welcome"
    }
    
    
    
@app.delete("/delete/{id}")
def delete_data(id : int):
    cursor.execute("""DELETE FROM posts WHERE id = %s""", (str(id),))
    conn.commit()
    
    return {
        "message" : "delete successfuly"
    }