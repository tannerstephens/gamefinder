from flask import Blueprint, request

from ..database import db
from ..lib import error_response
from ..models import Config, User

blueprint = Blueprint("setup", __name__, url_prefix="/setup")


@blueprint.route("/", methods=["POST"])
def first_time_setup():
    if Config.get():
        return error_response(405, "This app is not configurable")

    superuser_username = request.json["username"]
    superuser_password = request.json["password"]

    superuser = User(superuser_username, superuser_password, is_admin=True).save(False)
    Config(superuser).save()


@blueprint.route("/", methods=["GET"])
def setup_completed():
    if config := Config.get():
        return {"setup_completed": True, "config": config.serialize()}
    return {"setup_completed": False}
