from datetime import timedelta

from flask_jwt_extended import get_jwt_identity, create_access_token

from flask import Response


def new_access_token(response: Response):
    id = get_jwt_identity()
    if id is not None:
        response.headers['New-Access-Token'] = create_access_token(identity=id, expires_delta=timedelta(minutes=10))
        response.headers['Access-Control-Expose-Headers'] = 'New-Access-Token'
    return response
