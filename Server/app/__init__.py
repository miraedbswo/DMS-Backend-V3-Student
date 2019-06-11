from flask import Flask, jsonify
from jwt.exceptions import PyJWTError
from flask_jwt_extended.exceptions import JWTExtendedException

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
    flask_app.register_error_handler(JWTExtendedException, jwt_handle)
    flask_app.register_error_handler(PyJWTError, jwt_handle)

    from app.hook.before_request import check_secret_header
    flask_app.before_request(check_secret_header)


def register_blueprint(flask_app: Flask):
    from app.view.account import account_blueprint, info_blueprint
    flask_app.register_blueprint(account_blueprint)
    flask_app.register_blueprint(info_blueprint)

    from app.view.apply import apply_blueprint
    flask_app.register_blueprint(apply_blueprint)

    from app.view.meal import meal_blueprint
    flask_app.register_blueprint(meal_blueprint)

    from app.view.notice import notice_blueprint
    flask_app.register_blueprint(notice_blueprint)

    from app.view.report import report_blueprint
    flask_app.register_blueprint(report_blueprint)

    from app.view.survey import survey_blueprint
    flask_app.register_blueprint(survey_blueprint)


def create_app(config_name: str) -> Flask:
    flask_app = Flask(__name__)
    flask_app.config.from_object(config[config_name])

    register_extension(flask_app)
    register_hook(flask_app)
    register_blueprint(flask_app)

    return flask_app


def wrong_token_handler(wrong_token: str):
    return jsonify({
        'status': 403,
        'sub_status': 42,
        'msg': 'Wrong Token'
    }), 403


def jwt_handle(e: Exception):
    return str(e), 403
