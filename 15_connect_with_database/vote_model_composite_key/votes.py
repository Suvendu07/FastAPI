from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .import auth, schema, models,oauth
from .database import get_db


router2 = APIRouter(
    prefix="/vote",
    tags=['vote']
)


@router2.post("/vote", status_code=status.HTTP_201_CREATED)
def vote(vote : schema.Vote, db : Session = Depends(get_db), current_user : int = Depends(oauth.get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    
    if not post:
        raise HTTPException(status_code=404, detail="post does't exist")
    
    
    vote_query = db.query(models.Post).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    
    found_vote = vote_query.first()
    
    
    if (vote.dir == 1):
          
     if found_vote:
        raise HTTPException(status_code=409, detail="vote already exist")
    
     new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id)
    
     db.add(new_vote)
     db.commit()
    
     return {
        "message" : "added successfuly"
     }
    
    else:
        if not found_vote:
            raise HTTPException(status_code=404, detail="vote not found")
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        
        return{
            "message" : "delete successfuly"
        }