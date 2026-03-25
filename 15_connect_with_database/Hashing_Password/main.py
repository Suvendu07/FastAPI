from fastapi import FastAPI, Response, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.params import Body
import psycopg2
import time
from psycopg2.extras import RealDictCursor
from .database import Base, get_db, engine
from .model import User
from .schema import UserCreate, UserOut
from .utils import pwd_context, hash
from dotenv import load_dotenv
import os
import time



load_dotenv()



# This is create engine and create model
Base.metadata.create_all(bind = engine)


app = FastAPI()




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
        print("database successfully")
        break
    
    except Exception as error:
        print("Connection failed")
        print(f"Error:",error)
        time.sleep(2)
        
        
        
@app.post("/users", response_model=UserOut)
def create_user(user : UserCreate, db: Session = Depends(get_db)):
    
    
    """Hashing password"""
    hashed_password = hash(user.password)
    user.password = hashed_password
    
    
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user




# Get user by ID
@app.get("/user{id}", response_model=UserOut)
def get_user(id : int, db : Session = Depends(get_db)):
    
    data = db.query(User).filter(User.id == id).first()
    
    
    if not data:
        raise HTTPException(status_code=404, detail="invlid id")
    
    return data
