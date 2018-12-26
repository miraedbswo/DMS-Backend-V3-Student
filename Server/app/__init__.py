from flask import Flask
from Server.app.view import Router


def create_app():
    app = Flask(__name__)

    Router(app).register_blueprint()

    return app
