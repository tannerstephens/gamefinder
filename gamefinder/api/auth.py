from flask import Blueprint, g, request, session

from ..lib import api_response, error_response
from ..models import User

blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@blueprint.route("/", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]

    user = User.get_by_uername(username)

    if user is None or not user.check_password(password):
        return error_response(401, "Invalid username or password")

    session["user_id"] = user.id

    return api_response({"user": user.serialize()})


@blueprint.route("/", methods=["GET"])
def get_login():
    data = None
    if g.user:
        data = g.user.serialize()
    return api_response({"user": data})


@blueprint.route("/", methods=["DELETE"])
def logout():
    session.clear()

    return api_response({"user": None})
