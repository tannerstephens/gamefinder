import os
from functools import lru_cache


class BaseConfig:
    DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///./gamefinder.db"


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
