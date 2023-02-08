from flask import Blueprint

from . import admin, auth, games, setup, users

blueprint = Blueprint("api", __name__, url_prefix="/api")

blueprint.register_blueprint(admin.blueprint)
blueprint.register_blueprint(auth.blueprint)
blueprint.register_blueprint(games.blueprint)
blueprint.register_blueprint(setup.blueprint)
blueprint.register_blueprint(users.blueprint)
