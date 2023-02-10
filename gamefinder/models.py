import enum
import os
import re
import textwrap
from hashlib import pbkdf2_hmac

from sqlalchemy import (
    Boolean,
    Column,
    Enum,
    ForeignKey,
    Index,
    Integer,
    String,
    Table,
    UnaryExpression,
    UniqueConstraint,
    func,
)
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

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

    @classmethod
    def paged(cls, page: int = 1, per_page: int = 20, order_by: UnaryExpression = None):
        query = db.session.query(cls)

        if order_by is not None:
            query = query.order_by(order_by)

        return query.offset((page - 1) * per_page).limit(per_page).all()

    @classmethod
    def count(cls):
        return db.session.query(cls).count()


class User(BaseModel, db.Base):
    PASSWORD_REGEX = re.compile(r"[a-zA-Z0-9*.!@#$%^&(){}\[\]:;<>,.?\/~_+\-=|\\]{8,}")

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
    def hash_password(password: str, salt: bytes | None = None) -> bytes:
        if salt is None:
            salt = os.urandom(32)
        key = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)

        return salt + key

    def check_password(self, password: str) -> bool:
        salt = self.password_hash[:32]

        return self.hash_password(password, salt) == self.password_hash

    def serialize(self):
        return dict(id=self.id, username=self.username, is_admin=self.is_admin)

    @classmethod
    def get_by_uername(cls, username: str):
        return (
            db.session.query(cls)
            .filter(func.lower(cls.username) == username.lower())
            .first()
        )

    @classmethod
    def is_valid_password(cls, password: str):
        return cls.PASSWORD_REGEX.match(password) is not None


username_lower_index = Index("username_lower_index", func.lower(User.username))

game_tags = Table(
    "game_tags",
    db.Base.metadata,
    Column("game_id", ForeignKey("games.id"), index=True, primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), index=True, primary_key=True),
)


class Tag(BaseModel, db.Base):
    __tablename__ = "tags"
    value: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)

    games: Mapped[list["Game"]] = relationship(
        secondary=game_tags, back_populates="tags"
    )

    __table_args__ = (UniqueConstraint("type", "value", name="_value_type_uc"),)

    def __init__(self, value: str, type: str):
        self.value = value
        self.type = type

    @classmethod
    def get_or_create_by(cls, value: str, type: str):
        tag = db.session.query(cls).filter(cls.value == value, cls.type == type).first()

        if tag is None:
            tag = cls(value, type)

        return tag

    def serialize(self):
        return {
            "value": self.value,
            "type": self.type,
        }


class Game(BaseModel, db.Base):
    __tablename__ = "games"
    shelf_id: Mapped[int] = mapped_column(ForeignKey("shelves.id"))
    shelf: Mapped["Shelf"] = relationship("Shelf", back_populates="games")

    shelf_row: Mapped[int] = mapped_column(nullable=False)
    shelf_column: Mapped[int] = mapped_column(nullable=False)

    bgg_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    thumbnail: Mapped[str] = mapped_column(String)
    image: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    year: Mapped[int] = mapped_column(Integer)
    min_players: Mapped[int] = mapped_column(Integer)
    max_players: Mapped[int] = mapped_column(Integer)
    best_players: Mapped[str] = mapped_column(Integer)
    min_playtime: Mapped[int] = mapped_column(Integer)
    max_playtime: Mapped[int] = mapped_column(Integer)
    min_age: Mapped[int] = mapped_column(Integer)

    tags: Mapped[list["Tag"]] = relationship(
        secondary=game_tags, back_populates="games"
    )

    def __init__(
        self,
        bgg_id: str,
        name: str,
        shelf: "Shelf",
        shelf_row: int,
        shelf_column: int,
        image: str | None = None,
        thumbnail: str | None = None,
        description: str | None = None,
        year: int | None = None,
        min_players: int | None = None,
        max_players: int | None = None,
        best_players: int | None = None,
        min_playtime: int | None = None,
        max_playtime: int | None = None,
        min_age: int | None = None,
    ):
        self.bgg_id = bgg_id
        self.name = name
        self.image = image
        self.thumbnail = thumbnail
        self.description = description
        self.year = year
        self.min_players = min_players
        self.max_players = max_players
        self.best_players = best_players
        self.min_playtime = min_playtime
        self.max_playtime = max_playtime
        self.min_age = min_age
        self.shelf = shelf
        self.shelf_row = shelf_row
        self.shelf_column = shelf_column

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "thumbnail": self.thumbnail,
            "description": self.description,
            "short_description": textwrap.shorten(self.description, width=150),
            "year": self.year,
            "min_players": self.min_players,
            "max_players": self.max_players,
            "best_players": self.best_players,
            "min_playtime": self.min_playtime,
            "max_playtime": self.max_playtime,
            "min_age": self.min_age,
            "tags": [tag.serialize() for tag in self.tags],
            "location": {
                "shelf": self.shelf.name,
                "row": self.shelf_row,
                "col": self.shelf_column,
            },
        }

    @classmethod
    def get_by_bgg_id(cls, bgg_id: int):
        return db.session.query(cls).filter(cls.bgg_id == bgg_id).first()


class ShelfTypes(enum.Enum):
    standard = "standard"
    cube = "cube"


class Shelf(BaseModel, db.Base):
    __tablename__ = "shelves"
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    type: Mapped[ShelfTypes] = mapped_column(Enum(ShelfTypes), nullable=False)
    width: Mapped[int] = mapped_column(Integer)
    height: Mapped[int] = mapped_column(Integer)
    games: Mapped[list["Game"]] = relationship("Game", back_populates="shelf")

    def __init__(self, name: str, type: str, width: int, height: int):
        self.name = name
        self.type = type
        self.width = width
        self.height = height

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type.value,
            "width": self.width,
            "height": self.height,
        }

    @classmethod
    def get_by_name(cls, name: str):
        return db.session.query(cls).filter(cls.name == name).first()


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
