from flask import Blueprint, request

from gamefinder.lib import api_response, error_response
from gamefinder.models import Shelf

blueprint = Blueprint("shelves_admin", __name__, url_prefix="/shelves")


@blueprint.route("/", methods=["POST"])
def create_shelf():
    shelf_name = request.json.get("name")

    if Shelf.get_by_name(shelf_name) is not None:
        return error_response(400, "A shelf with this name already exists")

    shelf_type = request.json.get("type")
    width = request.json.get("width")
    height = request.json.get("height")

    if width < 1 or height < 1:
        return error_response(400, "Width and height must be > 0")

    shelf = Shelf(shelf_name, shelf_type, width, height).save()

    return api_response({"shelf": shelf.serialize()})


@blueprint.route("/", methods=["GET"])
def list_shelves():
    return api_response({"shelves": [shelf.serialize() for shelf in Shelf.all()]})
