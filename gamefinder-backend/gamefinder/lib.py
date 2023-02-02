from .models import Config, User


def error_response(status: int, description: str):
    return {"description": description}, status


def is_superuser(user: User) -> bool:
    return Config.get().superuser is user
