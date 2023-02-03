from flask import Blueprint

from . import setup, users

blueprint = Blueprint("api", __name__, url_prefix="/api")

blueprint.register_blueprint(users.blueprint)
blueprint.register_blueprint(setup.blueprint)
