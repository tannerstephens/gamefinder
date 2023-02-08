from math import ceil

from flask import Blueprint, request

from ..lib import api_response, error_response
from ..models import Game

blueprint = Blueprint("games", __name__, url_prefix="/games")


@blueprint.route("/", methods=["GET"])
def list_games():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 20))

    games = Game.paged(page, per_page, order_by=Game.name.asc())
    total_games = Game.count()

    total_pages = ceil(total_games / per_page)

    resp = api_response(
        {"games": [game.serialize() for game in games], "total_pages": total_pages}
    )

    return resp


@blueprint.route("/<int:game_id>", methods=["GET"])
def get_game(game_id: int):
    if (game := Game.get_by_id(game_id)) is None:
        return error_response(404, "Game not found")

    return api_response({"game": game.serialize()})
