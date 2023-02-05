from flask import Flask, g, session

from .models import User


def before_request(app: Flask):
    @app.before_request
    def load_user():
        user = None
        if user_id := session.get("user_id"):
            user = User.get_by_id(user_id)

            if user is None:
                session.clear()

        g.user = user
