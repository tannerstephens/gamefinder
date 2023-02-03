from flask import Blueprint, request

from ..database import db
from ..lib import error_response
from ..models import User

blueprint = Blueprint("users", __name__, url_prefix="/users")


@blueprint.route("/", methods=["GET"])
def list_users():
    users = db.session.query(User).all()

    print("users")

    return [user.serialize() for user in users]


@blueprint.route("/", methods=["POST"])
def create_user():
    username = request.json["username"]
    if User.get_by_uername(username):
        return error_response(400, "Username already registered")
    password = request.json["password"]
    new_user = User(username, password).save()
    return new_user.serialize()
