from flasgger import swag_from
from flask import current_app, request, jsonify
from flask_jwt_extended import jwt_refresh_token_required

from app.doc.account.auth import AUTH_POST
from app.model import StudentModel, TokenModel
from app.util.json_schema import json_type_validate, AUTH_POST_JSON
from app.view.base_resource import AccountResource


class AuthView(AccountResource):
    @json_type_validate(AUTH_POST_JSON)
    @swag_from(AUTH_POST)
    def post(self):
        student = StudentModel.login(request.json['id'], request.json['password'])
        access_token = create_access_token(student.id, expires_delta=timedelta(hours=1))
        refresh_token = create_refresh_token(student.id, expires_delta=timedelta(days=30))
        return jsonify(
            {
                'accessToken': access_token,
                'refreshToken': refresh_token
            }
        )
    @jwt_refresh_token_required
    def post(self):
        user_agent = request.headers.get('user-agent')
        authorization = request.headers.get(current_app.config['JWT_HEADER_NAME'])
        refresh_token = authorization[7:]
        token = TokenModel.create_refresh_token(refresh_token, user_agent)

        return jsonify(token)


