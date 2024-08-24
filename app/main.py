
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models
from .database import engine
from .routers import user, post, auth, vote
from .config import settings


app = FastAPI(title = "Social Media App", version="1.1.0")
# Always keep in mind when structuring your APIs. It runs from top to bottom.

# Creating tables in datebase
# models.Base.metadata.create_all(bind=engine)

# CORS policy allows you to make resuest from the same server 
# By default, our API allows web browser running on same domain as our server to make request.

# Java Script Console
# fetch("http:localhost:8000").then(res => res.json()).then(console.log)
origins = [
    "*",  # example it can be accessed from anywhere, wild card, all connections allowed.
    # 'https://www.google.com' # Example 
    # "https://www.youtube.com"
]

# Cross - Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # http method , * > wild card
    allow_headers=["*"], #
)



@app.get("/", tags=["Root"])
def read_root():
    return {"Hello": "World"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)



    

