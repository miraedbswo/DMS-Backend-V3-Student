from datetime import timedelta
from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from flasgger import swag_from

from app.doc.account.auth import AUTH_POST
from app.view.base_resource import AccountResource
from app.model import StudentModel
from app.util.json_schema import json_type_validate, AUTH_POST_JSON


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
