from flask import Blueprint, request

import gamefinder.bgg as bgg
from gamefinder.lib import api_response, error_response
from gamefinder.models import Game, Shelf, Tag

blueprint = Blueprint("games_admin", __name__, url_prefix="/games")


@blueprint.route("/", methods=["POST"])
def create_game():
    game_id = request.json["game_id"]
    shelf_id = request.json["shelf_id"]
    row = request.json["row"]
    column = request.json["column"]

    thing = bgg.thing(game_id)

    if thing is None:
        return error_response(404, "Game not found")

    shelf = Shelf.get_by_id(shelf_id)

    if row < 1 or row > shelf.height:
        return error_response(400, "Row must be in range of the shelf height")

    if column < 1 or column > shelf.width:
        return error_response(400, "Row must be in range of the shelf width")

    tag_dicts = thing.pop("tags")

    tags = [Tag.get_or_create_by(**tag_dict).save(False) for tag_dict in tag_dicts]
    game = Game(shelf=shelf, shelf_row=row, shelf_column=column, **thing)

    game.tags = tags
    game.save()

    return api_response({"game": game.serialize()})
