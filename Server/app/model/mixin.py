from datetime import datetime, timedelta

from app.extension import db
from app.exception import BadRequestException


class BaseMixin:

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def kst_now():
        return datetime.utcnow() + timedelta(hours=9)

    @staticmethod
    def assert_validation(validate_result: bool):
        if not validate_result:
            raise BadRequestException()
