from time import time

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    decode_token,
    get_jwt_identity
)

from app.exception import ForbiddenException
from app.extension import db
from app.model.mixin import BaseMixin


class TokenModel(db.Model, BaseMixin):
    __tablename__ = 'token'
    owner: str = db.Column(db.String, db.ForeignKey('student.id', ondelete='CASCADE'))
    refresh_token: str = db.Column(db.String, primary_key=True)
    user_agent: str = db.Column(db.String, primary_key=True)

    def __init__(self, owner: str, refresh_token: str, user_agent: str):
        self.owner: str = owner
        self.refresh_token: str = refresh_token
        self.user_agent: str = user_agent

    @classmethod
    def find_refresh_token(cls, owner: str, user_agent: str):
        return TokenModel.query.filter_by(owner=owner, user_agent=user_agent).first()

    @classmethod
    def _verify_refresh_token(cls, refresh_token, user_agent):
        token = TokenModel.query.filter_by(
            owner=get_jwt_identity(),
            refresh_token=refresh_token,
            user_agent=user_agent
        ).first()

        if not token:
            raise ForbiddenException()

        return token

    @classmethod
    def create_new_token(cls, owner: str, user_agent: str) -> dict:
        new_access_token = create_access_token(owner)
        new_refresh_token = create_refresh_token(owner)

        exist_token = cls.find_refresh_token(owner, user_agent)
        if exist_token:
            exist_token.delete()

        TokenModel(
            owner=owner,
            refresh_token=new_refresh_token,
            user_agent=user_agent
        ).save()

        return {
            'accessToken': new_access_token,
            'refreshToken': new_refresh_token
        }

    @classmethod
    def create_refresh_token(cls, refresh_token, user_agent):
        new_token = {}
        token = cls._verify_refresh_token(refresh_token, user_agent)
        token_data = decode_token(refresh_token)

        new_access_token = create_access_token(token_data.identity)
        new_token['accessToken'] = new_access_token

        # refresh token 의 유효 기간이 3일 미만일 경우 refresh_token 또한 재발급.
        if (time() - token_data.get('exp')) < 259200:
            new_refresh_token = create_refresh_token(token_data.identity)
            token.refresh_token = new_refresh_token
            new_token['refreshToken'] = new_refresh_token

            db.session.commit()

        return new_token
