from pydantic import BaseModel,EmailStr
from datetime import datetime
from pydantic.types import conint




class UserLogin(BaseModel):
    id : int



class UserResponse(UserLogin):
    title : str
    content : str
    published : bool = True
    created_at : datetime
    
    
    class config():
        orm_mode = True


class PostCreate(BaseModel):
    title : str
    content : str
    published : bool = True
    
    
    
    
    
class UserOut(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime
    
    
    class Config():
       orm_mode = True
    
class POst(PostCreate):
    id : int
    created_at : datetime
    owner_id : int
    owner : UserOut
    

    class Config:
       orm_mode = True
       
       
class PostUpdate(PostCreate):
    owner_id : int
    pass
    
class Vote(BaseModel):
    post_id : int
    dir : conint(ge=0, le=1)