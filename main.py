from random import randrange
from typing import Union, Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel # Defining data schema - validation
import numpy as np

app = FastAPI()
# Always keep in mind when structuring your APIs. It runs from top to bottom.
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

@app.get("/posts/latest/")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

# path parameter
@app.get("/posts/{id}/")
def get_posts(id: int, response: Response): 
    
    assert type(id) == int
    post = [entry for entry in my_posts if entry['id'] == id]
    
    if not post:
        # one way
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id {id} not found."}
        # other way
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                      detail=f"post with id {id} not found.")

    return {"post_details": post}
    

@app.get("/posts/")
def get_all_posts():
    return {"data": my_posts}

# 1. Defining without schema validation
# @app.post("/create_post/")
# def create_post(payload: dict = Body(...)):  Method 1:
    # print(payload)
    # return {"data": f"title: {payload["title"]}, content: {payload["content"]}"}

# 2. Defining the schema of the input data - This will also do the data validation.
@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):    
    
    print(post)
    print(post.dict())
    print(post.model_dump())
    # print(f"title: {new_post.title},  content : {new_post.content}")
    post_dict = post.model_dump()
    post_dict["id"] = randrange(1, 10000)
    
    my_posts.append(post_dict)
    
    
    
    return {"data": post_dict}
