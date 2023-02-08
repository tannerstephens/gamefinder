from .models import Config, User


def error_response(status: int, description: str):
    return {"success": False, "description": description}, status


def api_response(data: dict, status=200):
    data.update({"success": True})

    return data, status


def is_superuser(user: User) -> bool:
    return Config.get().superuser is user


def validate_password(password: str) -> bool:
    return len(password) >= 8
