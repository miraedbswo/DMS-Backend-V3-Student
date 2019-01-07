import hashlib
import re

from app.extension import db
from app.model.mixin import BaseMixin


class UnsignedStudentModel(db.Model, BaseMixin):
    __tablename__ = 'unsigned_student_model'
    uuid = db.column(db.String, primary_key=True)
    name = db.column(db.String)
    number = db.column(db.Integer)
    email = db.column(db.String)

    def __init__(self, name, number, email):
        self.uuid = UnsignedStudentModel.generate_uuid(email)
        self.name = name
        self.number = number
        self.email = email

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

        assert 1 <= grade <= 3 and 1 <= class_ <= 4 and 1 <= number_ <= 21
        return number

    @db.validates('email')
    def validate_email(self, key, email):
        assert re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@dsm.hs.kr$", email) is not None
        return email
