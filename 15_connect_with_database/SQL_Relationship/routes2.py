"""In this file we learn advanced querry like only the login user fetch, modify, retrive only there data """

from fastapi import APIRouter, Depends, HTTPException, status, Response
from .database import get_db
from .models import User, Post
from .oauth import get_current_user
from sqlalchemy.orm import Session
from .import shema


router = APIRouter()


# in this route only fetch the login user data
@router.get("/posts")
def login_user_post(db : Session = Depends(get_db), current_user : int = Depends(get_current_user)):
    
    data = db.query(Post).filter(Post.owner_id == current_user.id).all()
    
    return data



# in this route get user by id as the login user
@router.get("/getid/{id}", response_model=shema.POst)
def get_ids(id : int, db : Session = Depends(get_db), current_user : int = Depends(get_current_user)):
    new_data = db.query(Post).filter(Post.id == id).first()
    
    if new_data is None:
        raise HTTPException(status_code=404, detail="Post not found")
    
    if new_data.owner_id != current_user.id:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorize to perform requested action.")
   
   
    return new_data



# in this route only the login user delete there own posts, he can't delete any other posts
@router.delete("/delete/{id}")
def delete_post(id : int, db : Session = Depends(get_db), current_user : int = Depends(get_current_user)):
    
    post_query = db.query(Post).filter(Post.id == id)
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorize to perform request action")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)



# in this route modify there own data only the login user
@router.put("/update/{id}")
def update_data(id : int, update_post : shema.PostUpdate,db : Session = Depends(get_db), current_user : int = Depends(get_current_user)):
    
    post_query = db.query(Post).filter(Post.id == id)
    post = post_query.first()
    
    
    if post == None:
        raise HTTPException(status_code=404, detail="post id not found")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not perform action")
    
    post_query.update(update_post.dict(), synchronize_session=False)
    db.commit()
    
    return{
        "data": post_query.first()
    }