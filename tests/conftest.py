from pyexpat import model
from turtle import title
import pytest
from sqlalchemy import create_engine
from app.main import app
from fastapi.testclient import TestClient
from app.config import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db, Base
from app.oauth2 import create_access_token
from app import schemas, models

# Setting up test database instead
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:267766ks@localhost:5432/fastapi_test"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

# print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session():
    # alembic can also be used.
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    # Run our code before we run test client
    yield TestClient(app)
    # Run our code after we run test client


@pytest.fixture
def user(client):
    response = client.post(
        "/users/", json={"email": "test@gmail.com", "password": "password"}
    )
    new_user = response.json()
    new_user["password"] = "password"

    assert response.status_code == 201
    return new_user


@pytest.fixture
def token(user):
    return create_access_token({"userid": user["id"]})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {**client.headers, "Authorization": f"Bearer {token}"}
    return client


@pytest.fixture
def test_posts(user, session):
    posts = [
        {"title": "1st title", "content": "1st content ", "owner_id": user["id"]},
        {"title": "2nd title", "content": "2nd content", "owner_id": user["id"]},
        {"title": "3rd title", "content": "3rd content", "owner_id": user["id"]},
    ]

    def create_post_model(post):
        return models.Post(
            title=post["title"], content=post["content"], owner_id=post["owner_id"]
        )
        
    posts_map = map(create_post_model, posts)
    posts_list = list(posts_map)
    session.add_all(posts_list)

    # session.add_all(
    #     [
    #         models.Post(title="1st title", content="1st content", owner_id=user["id"]),
    #         models.Post(title="2nd title", content="2nd content", owner_id=user["id"]),
    #         models.Post(title="3rd title", content="3rd content", owner_id=user["id"]),
    #     ]
    # )

    session.commit()

    added_posts = session.query(models.Post).all()
    # .order_by(models.Post.title.desc()).all()

    return added_posts
