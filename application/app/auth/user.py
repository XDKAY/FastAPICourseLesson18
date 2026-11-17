import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from application.app.core.schemes.user import UserResponseScheme
from application.app.core.security.hash_password import hash_password_helper
from application.app.database.database import DATABASE

__all__ = ("auth_user", )

_security = HTTPBasic()


def auth_user(credentials: Annotated[HTTPBasicCredentials, Depends(_security)]) -> UserResponseScheme:
    credentials_auth_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Basic"},
    )

    for user in DATABASE:
        is_existing_user = secrets.compare_digest(
            credentials.username.encode("utf-8"),
            user.username.encode("utf-8")
        )

        if is_existing_user:
            if hash_password_helper.verify_password(credentials.password, user.hashed_password):
                return UserResponseScheme.model_validate(user)
            else:
                raise credentials_auth_error

    raise credentials_auth_error
