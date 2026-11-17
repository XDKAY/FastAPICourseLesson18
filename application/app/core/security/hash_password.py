from application.app.core.config.settings import settings
from passlib.context import CryptContext

__all__ = ("hash_password_helper", )


class HashPasswordHelper:
    def __init__(self, algorithms: list[str], deprecated: list[str]) -> None:
        self._context = CryptContext(
            schemes=algorithms,
            deprecated=deprecated,
        )

    def get_hash_password(self, value: str) -> str:
        return self._context.hash(value)

    def verify_password(self, value: str, hash_: str) -> bool:
        return self._context.verify(value, hash_)


hash_password_helper = HashPasswordHelper(
    algorithms=settings.crypto_context.algorithms,
    deprecated=settings.crypto_context.deprecated,
)
