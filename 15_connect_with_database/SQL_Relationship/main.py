from fastapi import FastAPI
from .database import Base,engine
from .models import Post
import psycopg2
from dotenv import load_dotenv
import os
from psycopg2.extras import RealDictCursor
from .import routes2, routes



load_dotenv()

Base.metadata.create_all(bind = engine)


while True:
    try:
        conn = psycopg2.connect(
            port = os.getenv("DB_PORT"),
            host = os.getenv("DB_HOST"),
            password = os.getenv("DB_PASSWORD"),
            user = os.getenv("DB_USER"),
            database = os.getenv("DB_NAME"),
            cursor_factory=RealDictCursor
            
        )
        print("database connected successfully")
        break
    
    except Exception as e:
        print("failed database connection")
        print(f"error: {e}")
        
app = FastAPI()


app.include_router(routes.router)
app.include_router(routes2.router)


"""In this folder we learn what is forign key how to create forigen key(models.py)  with the help of sqlalchemy and the relationship(1-2-many, many-2-1) like this(routes.py).

and also we learn advanced querry like only the login user can fetch only there data and delete only there data etc(routes2.py)."""