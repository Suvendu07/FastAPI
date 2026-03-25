from jose import JWTError, jwt
from datetime import timedelta, datetime
from dotenv import load_dotenv
import os


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data : dict):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    
    encoed_jwt = jwt.encode(to_encode,SECRET_KEY, algorithm=ALGORITHM)
    
    return encoed_jwt