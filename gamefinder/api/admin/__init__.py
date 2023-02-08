from flask import Blueprint, g

from gamefinder.lib import error_response

from . import games, search, shelves

blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@blueprint.before_request
def admin_required():
    if g.user is None or not g.user.is_admin:
        return error_response(401, "You do not have permission for this endpoint")


blueprint.register_blueprint(search.blueprint)
blueprint.register_blueprint(games.blueprint)
blueprint.register_blueprint(shelves.blueprint)
