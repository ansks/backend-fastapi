import jwt
from jwt.exceptions import PyJWTError
from datetime import datetime, timedelta, timezone
from fastapi import Depends, status, HTTPException
from . import schemas, database, models
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict):
    
    to_encode = data.copy()
    expire  = datetime.now(tz=timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, 
                             SECRET_KEY, 
                             algorithm=ALGORITHM)
    
    return encoded_jwt



def verify_access_token(token: str, credentials_exception):
    # verify access token: Algo, Secrect, accesstoken
    
    try:
        # print(token)
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        id: int = payload.get("user_id")        
        
        if id is None:
            raise credentials_exception
        
        token_data = schemas.TokenData(id=id)
    
    except PyJWTError as e:
        print(e)
        raise credentials_exception
    except AssertionError as e:
        print(e)
    
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    # get user details: access db using Depends
    
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                          detail="Could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    
    token = verify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()
    
    return user
    
    
    
    

    
    
    
    

