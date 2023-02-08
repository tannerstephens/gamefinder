from flask import Blueprint, request

from ..database import db
from ..lib import api_response, error_response, validate_password
from ..models import User

blueprint = Blueprint("users", __name__, url_prefix="/users")


@blueprint.route("/", methods=["GET"])
def list_users():
    users = db.session.query(User).all()

    return api_response({"users": [user.serialize() for user in users]})


@blueprint.route("/", methods=["POST"])
def create_user():
    username = request.json["username"]
    if User.get_by_uername(username):
        return error_response(400, "Username already registered")
    password = request.json["password"]

    if not validate_password(password):
        return error_response(400, "Your password must be at least 8 characters")

    new_user = User(username, password).save()
    return api_response({"user": new_user.serialize()})
