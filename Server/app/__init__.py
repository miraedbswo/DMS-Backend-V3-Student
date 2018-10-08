from flask import Flask
from Server.app.controller import Router


def create_app():
    app = Flask(__name__)

    Router(app).register_blueprint()

    return app
