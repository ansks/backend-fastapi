from fastapi import Body, Depends, FastAPI
from sqlalchemy.orm import Session

my_posts = [
    {"title": "black tea benifits", "content": "Antioxident properties", "id": 1},
    {"title": "yellow tea benifits", "content": "oxident properties", "id": 2}]

app = FastAPI()

@app.get("/sql_alchemy")
def test_post_db(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()
    
    return {"status": "success", 
            "data": post}
    
    
# 1. Defining without schema validation Method 1:
@app.post("/create_post/")
def create_post(payload: dict = Body(...)): 
    print(payload)
    return {"data": f"title: {payload["title"]}, content: {payload["content"]}"}

# 2. Defining the schema of the input data - This will also do the data validation.
    print(post)
    print(post.dict())
    print(post.model_dump())
    print(f"title: {new_post.title},  content : {new_post.content}")
    post_dict = post.model_dump()
    post_dict["id"] = randrange(1, 10000)
    
    my_posts.append(post_dict)
    return {"data": post_dict}
    
    # Putting in database
    # Method 1: f-string method -> exposed to SQL injection -> not advisable 
    cur.execute(f"""INSERT INTO posts (title, content, rating) VALUES ({post.title}, {post.content}, {post.rating}) RETURNING *""")