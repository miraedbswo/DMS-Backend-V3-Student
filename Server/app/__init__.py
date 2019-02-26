from flask import Flask, jsonify

from app.view import Router
from config import config


def register_extension(flask_app: Flask):
    from app import extension
    extension.db.init_app(flask_app)
    extension.jwt.init_app(flask_app)
    extension.jwt.invalid_token_loader(wrong_token_handler)
    extension.jwt.expired_token_loader(wrong_token_handler)
    extension.swag.init_app(flask_app)
    extension.swag.template = flask_app.config['SWAGGER_TEMPLATE']
    extension.cors.init_app(flask_app)


def register_hook(flask_app: Flask):
    from app import exception
    from app.hook.exception_handler import http_exception_handler
    flask_app.register_error_handler(exception.NoContentException, http_exception_handler)
    flask_app.register_error_handler(exception.ResetContentException, http_exception_handler)
    flask_app.register_error_handler(exception.WrongAuthException, http_exception_handler)
    flask_app.register_error_handler(exception.ApplyTimeException, http_exception_handler)
    flask_app.register_error_handler(exception.BadRequestException, http_exception_handler)

    from app.hook.after_request import new_access_token
    flask_app.after_request(new_access_token)

    from app.hook.before_request import check_secret_header
    flask_app.before_request(check_secret_header)


def create_app(config_name: str) -> Flask:
    flask_app = Flask(__name__)
    flask_app.config.from_object(config[config_name])

    register_extension(flask_app)
    register_hook(flask_app)
    Router(flask_app).register_blueprint()

    return flask_app


def wrong_token_handler(wrong_token: str):
    return jsonify({
        'status': 403,
        'sub_status': 42,
        'msg': 'Wrong Token'
    }), 403
