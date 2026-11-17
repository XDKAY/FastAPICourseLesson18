from typing import Annotated
from fastapi import FastAPI, Depends, status

from application.app.database.database import DATABASE
from application.app.core.security.hash_password import hash_password_helper
from application.app.core.schemes.user import (
    UserRequestScheme,
    UserResponseScheme,
    UserModel,
)
from application.app.auth.user import auth_user

__all__ = ("app", )

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Hello World!"
    }


@app.post("/register", status_code=status.HTTP_201_CREATED)
def register_endpoint(user: UserRequestScheme) -> dict[str, str]:
    user_model = UserModel(
        username=user.username,
        hashed_password=hash_password_helper.get_hash_password(user.password)
    )

    DATABASE.append(user_model)

    return {"message": f"Пользователь {user.username} был успешно зарегистрирован"}



@app.get("/login")
def login_endpoint(auth_user: Annotated[UserResponseScheme, Depends(auth_user)]) -> dict[str, str]:
    return {"message": f"Welcome, {auth_user.username}!"}
