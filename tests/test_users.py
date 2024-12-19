from fastapi import HTTPException, status
import pytest
from websockets import Data
from .database import client, session
from app import schemas
from app.oauth2 import verify_access_token


def test_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json().get("message") == "Hello World"


def test_create_user(client):
    response = client.post(
        "/users/", json={"email": "test@gmail.com", "password": "password"}
    )

    new_user = schemas.UserOut(**response.json())
    print(new_user)

    assert new_user.email == "test@gmail.com"
    assert response.status_code == 201


@pytest.mark.parametrize(
    "username, password, statuscode",
    [
        ("username", "password", 403),
        ("username", "passwor", 403),
        (None, "password", 422),
        (None, None, 422),
        ("test@gmail.com", "password", 200),
    ],
)
def test_login(user, client, username, password, statuscode):
    print(user)

    response = client.post("/login/", data={"username": username, "password": password})
    # print(response.json())

    assert response.status_code == statuscode

    if response.status_code == 200:
        res = response.json()
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        verified_user = verify_access_token(res["access_token"], credentials_exception)

        assert verified_user.id == user.get("id")
