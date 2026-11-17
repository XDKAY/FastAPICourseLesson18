import string

__all__ = ("is_valid_password", )


def is_valid_password(value: str) -> None:
    if not any(char in value for char in string.ascii_lowercase):
        raise ValueError("Пароль должен содержать хотя бы один символ нижнего регистра")

    if not any(char in value for char in string.ascii_uppercase):
        raise ValueError("Пароль должен содержать хотя бы один символ верхнего регистра")

    if not any(char in value for char in string.digits):
        raise ValueError("Пароль должен содержать хотя бы одну цифру")

    if not any(char in value for char in string.punctuation):
        raise ValueError("Пароль должен содержать хотя бы один знак пунктуации")
