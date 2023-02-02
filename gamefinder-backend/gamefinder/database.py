from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


class Database:
    def __init__(self, app: Flask | None = None):
        if app:
            self.init_app(app)

    def init_app(self, app: Flask):
        self.engine = create_engine(app.config["DATABASE_URI"])
        self.session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )

        self.Base = declarative_base()

    def create_all(self):
        import gamefinder.models

        self.Base.metadata.create_all(bind=self.engine)


db = Database()
