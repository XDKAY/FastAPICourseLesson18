from typing import Annotated
from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
    field_validator,
)

from application.app.core.utils.validator_password import is_valid_password


class UserBaseScheme(BaseModel):
    username: Annotated[str, Field(examples=["username"], min_length=3, max_length=20)]

    @field_validator("username")
    @classmethod
    def _validator_username(cls, value: str) -> str:
        if not value.isalpha():
            raise ValueError("Имя пользователя должно состоять только из букв")

        return value


class UserRequestScheme(UserBaseScheme):
    password: Annotated[str, Field(examples=["qwerty123!ABC"], min_length=8, max_length=20)]

    @field_validator("password")
    @classmethod
    def _validator_password(cls, value: str) -> str:
        is_valid_password(value)
        return value


class UserModel(UserBaseScheme):
    hashed_password: str


class UserResponseScheme(UserBaseScheme):
    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore"
    )
