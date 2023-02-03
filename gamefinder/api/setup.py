from flask import Blueprint, request

from ..lib import error_response
from ..models import Config, User

blueprint = Blueprint("setup", __name__, url_prefix="/setup")


@blueprint.route("/", methods=["POST"])
def first_time_setup():
    print("setup")
    if Config.get():
        return error_response(405, "This app is not configurable")

    superuser_username = request.json["username"]
    superuser_password = request.json["password"]

    superuser = User(superuser_username, superuser_password, is_admin=True).save(False)
    config = Config(superuser).save()

    return {"setup_completed": True, "config": config.serialize()}


@blueprint.route("/", methods=["GET"])
def setup_completed():
    setup_completed = False
    config_data = {}
    if config := Config.get():
        setup_completed = True
        config_data = config.serialize()
    return {"setup_completed": setup_completed, "config": config_data}
