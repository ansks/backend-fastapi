from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import psycopg
from psycopg.rows import dict_row
import logging
from .config import settings

# SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip-address/hostname>/<database_name>"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# Setting up database # It should be read from config.ini file 
def manual_setup():
    while True:
        try:
            uri = SQLALCHEMY_DATABASE_URL
            conn = psycopg.connect(uri, row_factory=dict_row)
            cur = conn.cursor()
            logging.info("Database connection established.")
            break
        
        except Exception as e:
            print("Database connection failed.")
            print(f"Following error {e} happended")
            time.sleep(2)

# print(cur.execute('select * from posts').fetchone())

# Establishing a connection 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    # connect_args={"check_same_thread": False} # for SQL-lite when running in memory
)

SessionLocal = sessionmaker(autocommit=False, 
                            autoflush=False, 
                            bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


