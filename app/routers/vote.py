# Vote Route:
"""
- path /vote
- user should be extracted from JWT token 
- Body will contain the id of the post that user want to vote and direction
{
    "post_id": 10,
    "vote_dir": 0  # 0 means delete the vote, 1: add the vote
}
"""
from pyexpat import model
from fastapi import Depends, APIRouter, HTTPException, status
from httpx import delete, post
from .. import schemas, database, oauth2, models
from sqlalchemy.orm import Session

router = APIRouter(prefix="/votes", 
                   tags=['Votes'])


@router.post("/", status_code=status.HTTP_201_CREATED)
def votes(vote: schemas.Vote, 
         db: Session = Depends(database.get_db),
         current_user: int = Depends(oauth2.get_current_user)):
    
    # query db to check if post exist
    post_valid  = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    
    if not post_valid:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, 
                            detail=f"post with id {vote.post_id} doesnt exist.")
    
    # query db to check if vote exists
    vote_query = db.query(models.Vote)\
                    .filter(models.Vote.post_id == vote.post_id, 
                            models.Vote.user_id == current_user.id)
    
    vote_details = vote_query.first()            
            
    if vote_details:
        
        if vote.dir == 0:
            # vote_delete = models.Vote(user_id  = current_user.id, 
            #                           post_id = vote.post_id)
            vote_query.delete(synchronize_session=False)
            db.commit()
            
            return {"message": f"Vote from user {current_user.id} deleted"}
        
        ## vote exist check
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                                detail=f"vote already exist for post {vote_details.post_id} from user {vote_details.user_id}")
     
    # Adding vote if doesnot exist.
    vote_added = models.Vote(user_id = current_user.id, 
                             post_id = vote.post_id)
    db.add(vote_added)
    db.commit()
    db.refresh(vote_added)
    
    return {"message": f"Vote from user {current_user.id} for post {vote.post_id} added",
                    "vote_added": vote_added}
        
    
    
        
        
    
            
        
            
    
    
    
    # vote exist or not 
    print(vote_details)
    
    
    
    
