from pydantic import BaseModel, EmailStr, conint
from typing import Optional
from datetime import datetime

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[str] = None
class CreateUser(BaseModel):
    email: EmailStr
    password: str
    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:  # since we are connecting with the database
        from_attributes = True


class PostBaseModel(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
class CreatePost(PostBaseModel):
    pass

class UpdatePost(PostBaseModel):
    pass

class PostResponse(PostBaseModel):
    id: int
    created_at: datetime
    # owner_id: int
    owner: UserOut
    
    class Config:  # since we are connecting with the database
        from_attributes = True
        
class Login(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[int] = None
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
    
class VoteResponse(Vote):
    user_id: int
    

    

    