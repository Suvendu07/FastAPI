from fastapi import FastAPI
from dotenv import load_dotenv
import os
from psycopg2.extras import RealDictCursor
import psycopg2
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
        print("database connect successfully")
        break
        
    except Exception as error:
        print("connection failed")
        print(f"error {error}")
        time.sleep(2)
        

app = FastAPI(
    title="retrieve data"
)



@app.get("/")
def home_page():
    return {
        "message" : "Welcome"
    }
    
    
@app.get("/retrive")
def retrieve_data():
    cursor.execute("""SELECT * FROM posts""")
    new_data = cursor.fetchall()
    
    return new_data