from typing import List
from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from .. import models, schemas, utils
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",   # concatenats the next items 
    tags=["Users"])



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    
    # Hashing the password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    user_dict = user.model_dump()
    new_user = models.User(**user_dict)
    
    db.add(new_user) # Adding the data
    db.commit()
    db.refresh(new_user) # Same as returning statement
    
    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"user with id {id} not found")
    else:
        return user