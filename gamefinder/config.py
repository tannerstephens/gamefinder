import os
from functools import lru_cache


def get_secret_key():
    if not (key := os.environ.get("SECRET_KEY")):
        try:
            with open(".secret_key", "rb") as secret:
                key = secret.read()
        except (OSError, IOError):
            key = None

        if not key:
            key = os.urandom(64)
            # Attempt to write the secret file
            # This will fail if the filesystem is read-only
            try:
                with open(".secret_key", "wb") as secret:
                    secret.write(key)
                    secret.flush()
            except (OSError, IOError):
                pass

    return key


class BaseConfig:
    DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:////config/gamefinder.db"
    SECRET_KEY = get_secret_key()


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    pass


@lru_cache
def get_config():
    env = os.environ.get("ENV")

    if env == "prod":
        return ProdConfig()
    else:
        return DevConfig()
