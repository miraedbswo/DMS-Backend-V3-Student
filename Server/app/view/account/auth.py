from flasgger import swag_from
from flask import current_app, request, jsonify
from flask_jwt_extended import jwt_refresh_token_required

from app.doc.account.auth import AUTH_POST, REFRESH_POST
from app.model import StudentModel, TokenModel
from app.util.json_schema import json_type_validate, AUTH_POST_JSON
from app.view.base_resource import AccountResource


class Auth(AccountResource):
    @json_type_validate(AUTH_POST_JSON)
    @swag_from(AUTH_POST)
    def post(self):
        student = StudentModel.login(request.json['id'], request.json['password'])
        user_agent = request.headers.get('user-agent')
        token = TokenModel.create_new_token(student.id, user_agent)

        return jsonify(token)


class Refresh(AccountResource):
    @swag_from(REFRESH_POST)
    @jwt_refresh_token_required
    def post(self):
        user_agent = request.headers.get('user-agent')
        authorization = request.headers.get(current_app.config['JWT_HEADER_NAME'])
        refresh_token = authorization[7:]
        token = TokenModel.create_refresh_token(refresh_token, user_agent)

        return jsonify(token)

