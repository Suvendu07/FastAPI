from fastapi import HTTPException, Request, status, Depends
from jose import jwt, JWTError
from dotenv import load_dotenv
import os
from sqlalchemy.orm import Session
from .database import get_db
from .models import Post, User

load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


def get_current_user(request : Request, db : Session = Depends(get_db)):
    
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credential"
    )
    
    token = request.cookies.get("access_token")
    
    if not token:
        raise credential_exception
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id :str =  payload.get("sub")
        
        if user_id is None:
            raise credential_exception
        
        user = db.query(User).filter(User.id == int(user_id)).first()
        
    except JWTError:
        raise credential_exception
    
    return user