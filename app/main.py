from fastapi import FastAPI
from sqlalchemy.orm import Session
from . import models
from .database import engine
from .routers import user, post, auth
from .config import settings


app = FastAPI(title = "Social Media App", version="1.1.0")
# Always keep in mind when structuring your APIs. It runs from top to bottom.

# Creating tables in datebase
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)



    

