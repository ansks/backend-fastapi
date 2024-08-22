from typing import List, Optional
from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from .. import models, schemas, utils, oauth2
from ..database import get_db, engine
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/posts", 
    tags=["Posts"])


@router.get("/", response_model = List[schemas.PostResponse])
def get_all_posts(db: Session = Depends(get_db), 
                  limit: int = 10, # more parameters 
                  skip: int = 0,
                  search: Optional[str] = ''):
    
    # cur.execute(""" SELECT * FROM posts """)
    # posts = cur.fetchall()
    
    posts = db.query(models.Post)\
                .filter(models.Post.title.contains(search))\
                .limit(limit=limit)\
                .offset(offset=skip)\
                .all()
                
    
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(post: schemas.CreatePost,
                db: Session = Depends(get_db), 
                current_user: int = Depends(oauth2.get_current_user)):
    
    ######## DATABASE ##########    
    # Method : inbuilt method
    # query = """INSERT INTO posts (title, content, published, rating) VALUES (%s, %s, %s, %s) RETURNING *"""
    # cur.execute(query, (post.title, post.content, post.published, post.rating))
    # new_post = cur.fetchone()
    # conn.commit()

    # Method:
    post_dict = post.model_dump()
    post_dict.update({'owner_id': current_user.id})
    
    new_post = models.Post(**post_dict) 
    # title = post.title, content = post.content, published = post.published,rating = post.rating
    db.add(new_post) # Adding the data
    db.commit()
    db.refresh(new_post) # Same as returning statement
    
    return new_post


@router.get("/latest/", status_code=status.HTTP_200_OK, response_model=schemas.PostResponse)
def get_latest_post(db: Session = Depends(get_db), 
                    current_user: int = Depends(oauth2.get_current_user)):
    # post = my_posts[len(my_posts)-1]
    
    # DATABASE
    # cur.execute(""" SELECT * FROM posts ORDER BY created_at DESC LIMIT 1 """)
    # post = cur.fetchone()
    
    #ORM
    post = db.query(models.Post).filter(models.Post.owner_id == current_user.id).order_by(models.Post.created_at.desc()).first()
    
    return post


# path parameter
@router.get("/{id}/", response_model = schemas.PostResponse)
# def get_posts(id: int, response: Response): 
def get_posts(id: int,
              db: Session = Depends(get_db),
              current_user: int = Depends(oauth2.get_current_user)):
    
    # assert type(id) == int
    # post = [entry for entry in my_posts if entry['id'] == id]
    
    ###### DATABASE
    # cur.execute("""SELECT * FROM posts where id = %s""", (str(id),))
    # post = cur.fetchone()
    # print(post)
    
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        # one way
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id {id} not found."}
        # other way
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                      detail=f"post with id {id} not found.")
    
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, 
                db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    
    ######## DATABASE ##########
    # cur.execute(""" DELETE FROM posts WHERE id=%s RETURNING *""", (str(id),))
    # delete_post = cur.fetchone()
    # conn.commit()
    
    delete_query = db.query(models.Post).filter(models.Post.id == id)
    delete_post = delete_query.first()
    
    # if not delete_post:
    if not delete_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    # Other user can not delete the post
    if current_user.id != delete_post.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="Server understood the request but refused to process it")
    
    delete_post.delete(synchronize_session = False)
    db.commit()
    
    
@router.put("/{id}", status_code=status.HTTP_201_CREATED, response_model= schemas.PostResponse)
def update_post(id: int, 
                post: schemas.UpdatePost, 
                db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    
    ##### DATABASE ####
    # post = post.model_dump()
    
    # cur.execute(""" UPDATE posts 
    #                 SET title = %s, content = %s 
    #                 WHERE id = %s RETURNING *""",
    #             (post['title'], post['content'], str(id)))

    # updated_post = cur.fetchone()
    # conn.commit()
    
    post_dict = post.model_dump()
    updated_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post  = updated_query.first()
    
    # if not updated_post:
    if not updated_post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id {id} was not found")
    
    if current_user.id != updated_post.owner_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="Server understood the request but refused to process it")
    #     # return {"data" : updated_post}
    updated_query.update(post_dict, synchronize_session=False)
    db.commit()
    return updated_query.first()
    #     return None