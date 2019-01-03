from flask import Flask
from app.view import Router
from config import config


def register_extension(flask_app: Flask):
    from app import extension
    extension.db.init_app(flask_app)
    extension.swag.init_app(flask_app)
    extension.swag.template = flask_app.config['SWAGGER_TEMPLATE']


def create_app(config_name: str) -> Flask:
    flask_app = Flask(__name__)
    flask_app.config.from_object(config[config_name])

    register_extension(flask_app)
    Router(flask_app).register_blueprint()

    return flask_app
