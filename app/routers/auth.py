from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .. import models, schemas, utils, oauth2
from .. import database
from sqlalchemy.orm import Session


router = APIRouter(tags=['Authentication'])

@router.post('/login/', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), 
          db: Session = Depends(database.get_db)):
    
    # Get user password from db -> error if not found in db
    # Get hash of new password and compare with hash -> error if not matched
    
    # OAuth2PasswordRequestForm returns {username, password} > in our case it username is email.
    # We dont send data using body rather, we will be using form-data
    
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid Credentials")
        
    elif not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid Credentials")
        
    else:
        access_token = oauth2.create_access_token(data={'user_id': user.id})
        
        return {"access_token": access_token, "token_type": "bearer"}