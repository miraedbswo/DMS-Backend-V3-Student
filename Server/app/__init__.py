from flask import Flask
from app.view import Router
from config import config


def register_extension(flask_app: Flask):
    from app import extension
    extension.db.init_app(flask_app)
    extension.jwt.init_app(flask_app)
    extension.swag.init_app(flask_app)
    extension.swag.template = flask_app.config['SWAGGER_TEMPLATE']
    extension.cors.init_app(flask_app)


def register_error_handler(flask_app: Flask):
    from app import exception
    from app.hook.exception_handler import http_exception_handler
    flask_app.register_error_handler(exception.NoContentException, http_exception_handler)
    flask_app.register_error_handler(exception.ResetContentException, http_exception_handler)
    flask_app.register_error_handler(exception.WrongAuthExcption, http_exception_handler)
    flask_app.register_error_handler(exception.ApplyTimeException, http_exception_handler)
    flask_app.register_error_handler(exception.BadRequestException, http_exception_handler)


def create_app(config_name: str) -> Flask:
    flask_app = Flask(__name__)
    flask_app.config.from_object(config[config_name])

    register_extension(flask_app)
    Router(flask_app).register_blueprint()

    return flask_app
