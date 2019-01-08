import bcrypt
import re
from typing import Union

from app.extension import db
from app.exception import NoContentException
from app.model.mixin import BaseMixin


class StudentModel(db.Model, BaseMixin):
    __tablename__ = 'student_model'
    id = db.column(db.String, primary_key=True)
    pw = db.column(db.String)
    name = db.column(db.String)
    number = db.column(db.Integer)
    email = db.column(db.String)

    def __init__(self, id: str, pw: str, name: str, number: number, email: str):
        self.id = id
        self.pw = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        self.name = name
        self.number = number
        self.email = email

    @staticmethod
    def get_student_by_id(id: str) -> 'StudentModel':
        return StudentModel.query.filter_by(id=id).first()

    @staticmethod
    def login(id: str, pw: str) -> Union[None, 'StudentModel']:
        student: StudentModel = StudentModel.get_student_by_id(id)
        if not student or not bcrypt.checkpw(pw, student.pw):
            raise NoContentException()
        return student

    @staticmethod
    def change_pw(id: str, current_pw: str, new_pw: str) -> bool:
        student: StudentModel = StudentModel.get_student_by_id(id)
        if bcrypt.checkpw(current_pw, student.pw):
            student.pw = bcrypt.hashpw(new_pw.encode(), bcrypt.gensalt())
            db.session.commit()
            return True
        return False

    @staticmethod
    def reset_pw(id: str):
        student: StudentModel = StudentModel.get_student_by_id(id)
        student.pw = bcrypt.hashpw('1234'.encode(), bcrypt.gensalt())
        db.session.commit()

    @db.validates('id')
    def validate_id(self, key, id):
        assert 4 <= len(id) <= 16
        return id

    @db.validates('number')
    def validate_pw(self, key, number):
        grade = number // 1000
        class_ = number // 100 % 10
        number_ = number % 100

        assert 1 <= grade <= 3 and 1 <= class_ <= 4 and 1 <= number_ <= 21
        return number

    @db.validates('email')
    def validate_email(self, key, email):
        assert re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@dsm.hs.kr$", email) is not None
        return email
