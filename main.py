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


######## CRUD - Create, Read, Update, Delete Operation##########
# Always plural while creating path operations
# Create - POST -> /posts -> app.post("/posts")
# Read -> GET -> app.get("/posts") or  app.get("/posts/{:id}")
# Update -> PUT (send all the fields to update the entry)/PATCH (change specific item) -> app.put("/posts/{:id}")
# Delete - DELETE -> 



    


    
    





















# print("Hello")

# x = '2' 

# def get_full_name(first_name: str, second_name: str):
#     return first_name.title() + " " + second_name.title()

# print(get_full_name("Anshul", "Singh"))

# from typing import Optional, Union


# # def say_hi(name: Optional[str]):
# # def say_hi(name: Union[str, None] = None):
# #     print(f"Hey {name}!")
    
# # say_hi()

# # Typing: 
# # Simple Types: (int, float, str, bool, bytes), 
# # Generic Types: list, set, tuple, dict
# # Optional, Union
# # Classes as type

# class Person:
    
#     def __init__(self, name: str) -> None:
#         self.name = name

# def get_one_person(one_person: Person):
#     return one_person.name + " man!"

# hello = Person("hello")


# print(get_one_person(one_person = hello))


# # Pydantic Models: data validation - declare the shape of the data as classes with attributes and each attribute has a type, gives you an object with all data 

# from datetime import datetime
# from pydantic import BaseModel

# class User(BaseModel):
#     id: int
#     name: str = "John Doe"
#     signup_ts: datetime | None
#     friends: list[int] = []
    
# external_data = {
#     "id": 1,
#     "name": "Anshul",
#     "signup_ts": "2015-06-01 12:22"
# }
    
# user = User(**external_data)
# print(user)


# from typing import Annotated

# def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
#     return f"hello {name}!"
    
# print(say_hello("aSnhul"))




