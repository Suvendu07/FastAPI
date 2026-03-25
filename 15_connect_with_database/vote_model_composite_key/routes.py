from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from .database import get_db
from .models import Post, User
from sqlalchemy.orm import Session
from .schema import  UserLogin, PostCreate
from typing import List
from .auth import create_access_token
from .oauth  import get_current_user

router = APIRouter()





@router.post("/login")
def login_user(response : Response,user_data : UserLogin, db : Session = Depends(get_db)):
    
    data = db.query(User).filter(User.id == user_data.id).first()
    
    if not data:
        raise HTTPException(status_code=400, detail="invalid credentials")
    
    access_token = create_access_token(
        {"sub": str(data.id)}
    )
    
    response.set_cookie(key = "access_token", value=access_token, httponly=True)
    
    return {
        "message" : "login successfully"
        
    }



"""Insert value"""

@router.post("/create")
def create_posts(post : PostCreate, db : Session = Depends(get_db), current_user : int = Depends(get_current_user)):
    
    new_post = Post(
        owner_id = current_user.id , **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post



"""In this file just we learn how to insert the data in forign key."""