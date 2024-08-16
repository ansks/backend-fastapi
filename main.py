from random import randrange
from typing import Union, Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel # Defining data schema - validation
import numpy as np

app = FastAPI()

# Defining Schema for Post 
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[str] = None

my_posts = [{"title": "black tea benifits", "content": "Antioxident properties", "id": 1}, 
           {"title": "yellow tea benifits", "content": "oxident properties", "id": 2}]


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts/{name}/")
def get_posts(name: int):
    return {"data": f"this is post:  {name}"}

@app.get("/posts/")
def get_all_posts():
    return {"data": my_posts}

# 1. Defining without schema validation
# @app.post("/create_post/")
# def create_post(payload: dict = Body(...)):  Method 1:
    # print(payload)
    # return {"data": f"title: {payload["title"]}, content: {payload["content"]}"}

# 2. Defining the schema of the input data - This will also do the data validation.
@app.post("/posts/")
def create_post(post: Post):    
    
    print(post)
    print(post.dict())
    print(post.model_dump())
    # print(f"title: {new_post.title},  content : {new_post.content}")
    post_dict = post.model_dump()
    post_dict["id"] = randrange(1, 10000)
    
    my_posts.append(post_dict)
    
    return {"data": post_dict}
