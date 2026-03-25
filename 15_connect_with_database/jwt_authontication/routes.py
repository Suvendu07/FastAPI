from fastapi import APIRouter, Depends, HTTPException, Response
from .schema import UserRegister, UserLogin
from fastapi.security import OAuth2PasswordRequestForm
from .database import get_db
from .models import suvendu, Base
from sqlalchemy.orm import Session
from .utils import hash_password, verify_password
from .auth import create_access_token
from .oauth import get_current_user


router = APIRouter()


@router.post("/posts")
def create_users(user : UserRegister, db : Session = Depends(get_db)):
    
    hashed_password = hash_password(user.password)
    
    data = suvendu(
        username = user.username,
        email = user.email,
        password = hashed_password
    )
    
    db.add(data)
    db.commit()
    db.refresh(data)
    
    return {
        "message" : "register successfully"
    }
    
    
    
@router.post("/login")
def login(response: Response, from_data : OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    db_user = db.query(suvendu).filter(suvendu.username == from_data.username).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username")

    if not verify_password(from_data.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    access_token = create_access_token(
        data={"sub": db_user.username}
    )
    
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    

    return {"access_token": access_token, "token_type": "bearer"}



# get all the user
@router.get("/getuser{id}")
def get_user(id : int, db : Session = Depends(get_db), current_user : Session = Depends(get_current_user)):
    
    data = db.query(suvendu).filter(suvendu.id == id).first()
    
    if not data:
        raise HTTPException(status_code=404, detail="not found")
    
    
    return data