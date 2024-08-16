# backend-fastapi

1. virtual environment: py -3 -m venv venv  or python3 -m venv venv <br><br>
2. actiavte virtual environment in terminal: source venv/scripts/activate <br>
3. start app server: uvicorn main:app

# Notes:
<!-- 
######## CRUD - Create, Read, Update, Delete Operation##########
# Always plural while creating path operations
# Create - POST -> /posts -> app.post("/posts")
# Read -> GET -> app.get("/posts") or  app.get("/posts/{:id}")
# Update -> PUT (send all the fields to update the entry)/PATCH (change specific item) -> app.put("/posts/{id}")
# Delete - DELETE -> app.delete("/posts/{id}")

# TYPING AND PYDANTIC
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



 -->