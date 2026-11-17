from pydantic import BaseModel

__all__ = ("settings", )


class CryptoContextSettings(BaseModel):
    algorithms: list[str] = ["argon2"]
    deprecated: list[str] = ["auto"]


class Settings(BaseModel):

    crypto_context: CryptoContextSettings = CryptoContextSettings()


settings = Settings()
