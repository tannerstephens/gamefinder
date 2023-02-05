import os
from hashlib import pbkdf2_hmac
from typing import Optional

from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import db


class BaseModel:
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            db.session.commit()

    @classmethod
    def get_by_id(cls, id: int):
        return db.session.query(cls).filter(cls.id == id).first()


class User(BaseModel, db.Base):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(
        String, unique=True, index=True, nullable=False
    )
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)

    def __init__(self, username: str, password: str, is_admin: bool = False):
        self.username = username
        self.password_hash = self.hash_password(password)
        self.is_admin = is_admin

    @staticmethod
    def hash_password(password: str, salt: Optional[bytes] = None) -> bytes:
        if salt is None:
            salt = os.urandom(32)
        key = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)

        return salt + key

    def check_password(self, password: str) -> bool:
        salt = self.password_hash[:32]

        return self.hash_password(password, salt) == self.password_hash

    def serialize(self):
        return dict(id=self.id, username=self.username)

    @classmethod
    def get_by_uername(cls, username: str):
        return db.session.query(cls).filter(cls.username == username).first()


class Game(BaseModel, db.Base):
    __tablename__ = "games"
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    shelf_id: Mapped[int] = mapped_column(ForeignKey("shelves.id"))
    shelf: Mapped["Shelf"] = relationship("Shelf", back_populates="games")


class Shelf(BaseModel, db.Base):
    __tablename__ = "shelves"
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    width: Mapped[int] = mapped_column(Integer)
    height: Mapped[int] = mapped_column(Integer)
    games: Mapped[list["Game"]] = relationship("Game", back_populates="shelf")


class Config(BaseModel, db.Base):
    __tablename__ = "config"

    superuser_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    superuser: Mapped["User"] = relationship("User")

    def __init__(self, superuser: User):
        self.superuser = superuser

    @classmethod
    def get(cls) -> "Config":
        return db.session.query(cls).first()

    def serialize(self):
        return {}
