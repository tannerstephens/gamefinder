from flask import Flask

from .config import get_config
from .database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    db.init_app(app)
    db.create_all()

    with app.app_context():
        from . import api

        app.register_blueprint(api.blueprint)

    return app
