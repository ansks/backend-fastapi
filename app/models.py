from sqlalchemy import Column, Integer, String, Boolean, DateTime, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import timezone, datetime
from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable = False)
    published = Column(Boolean, nullable=False, server_default='TRUE')
    rating = Column(Integer, nullable=False, server_default= text('0'))
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable = False, 
                        server_default=text('now()'))
    owner_id  = Column(Integer, 
                       ForeignKey(column="users.id", ondelete="CASCADE"),
                       nullable = False)
    
    owner = relationship("User")  # Returning data from User Class
    
    # created_at = Column(DateTime(timezone=True),
    #                     nullable = False, 
    #                     default=datetime.now(tz=timezone.utc))
    
    
    
class User(Base): 
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable = False, 
                        server_default=text('now()'))

    
