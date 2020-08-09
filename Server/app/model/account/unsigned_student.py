import hashlib
import re

from app.exception import NoContentException
from app.extension import db
from app.model.base import BaseMixin


class UnsignedStudentModel(db.Model, BaseMixin):
    __tablename__ = 'unsigned_student'
    uuid: str = db.Column(db.String(6), primary_key=True)
    name: str = db.Column(db.String(20))
    number: int = db.Column(db.Integer)
    email: str = db.Column(db.String(50), nullable=True)

    def __init__(self, name: str, number: int, email: str, uuid=None):
        self.uuid: str = UnsignedStudentModel.generate_uuid(email) if uuid is None else uuid
        self.name: str = name
        self.number: int = number
        self.email: str = email

    @staticmethod
    def get_unsigned_student(uuid: str) -> 'UnsignedStudentModel':
        unsigned_student = UnsignedStudentModel.query.filter_by(uuid=uuid).first()
        if unsigned_student is None:
            raise NoContentException()
        return unsigned_student

    @staticmethod
    def generate_uuid(key: str) -> str:
        while True:
            sha = hashlib.sha1()
            sha.update(key.encode())

            key = sha.hexdigest[:5]
            if not UnsignedStudentModel.query.filter_by(uuid=key).first():
                return key

    @db.validates('number')
    def validate_number(self, key, number):
        grade = number // 1000
        class_ = number // 100 % 10
        number_ = number % 100

        self.assert_validation(grade in (1, 2, 3))
        self.assert_validation(class_ in (1, 2, 3, 4))
        self.assert_validation(number_ in range(1, 21))

        return number

    @db.validates('email')
    def validate_email(self, key, email):
        self.assert_validation(re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@dsm.hs.kr$", email) is not None)
        return email
