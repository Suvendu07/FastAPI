from fastapi import FastAPI, Depends, HTTPException
from .database import Base, engine, get_db
from .models import suvendu
from dotenv import load_dotenv
from .routes import router
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import time


load_dotenv()


Base.metadata.create_all(bind = engine)

app = FastAPI()



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
        print("database connect successfuly")
        break
    
    except Exception as e:
        print("failed connection")
        print(f"error: {e}")
        time.sleep(2)
        
app.include_router(router)