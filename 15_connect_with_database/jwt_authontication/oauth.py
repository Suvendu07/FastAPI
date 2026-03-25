from fastapi import HTTPException, Request, status
from dotenv import load_dotenv
from jose import JWTError, jwt
import os


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHIM = os.getenv("ALGORITHIM")



load_dotenv()


def get_current_user(request : Request):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credential"
    )
    
    
    
    token = request.cookies.get("access_token")
    
    
    if not token:
        raise credential_exception
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHIM])
        username = payload.get("sub")
        
        
        if username is None:
            raise credential_exception
        
    
    except JWTError:
        raise credential_exception
    
    
    return username