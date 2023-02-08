from flask import Blueprint, request

import gamefinder.bgg as bgg
from gamefinder.lib import api_response

blueprint = Blueprint("bgg_search", __name__, url_prefix="/search")


BGG_BASE_URL = "https://boardgamegeek.com/xmlapi2"


@blueprint.route("/", methods=["GET"])
def search():
    query = request.args["query"]

    return api_response({"results": bgg.search(query)})
