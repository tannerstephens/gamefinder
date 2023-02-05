from flask import Flask, send_from_directory

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

    @app.route("/")
    def base():
        return send_from_directory("frontend/public", "index.html")

    @app.route("/<path:path>")
    def serve_frontend(path):
        return send_from_directory("frontend/public", path)

    from .before_request import before_request

    before_request(app)

    return app
