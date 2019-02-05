import bcrypt
import re
from typing import Union

from app.extension import db
from app.exception import NoContentException, ResetContentException, WrongAuthExcption, ForbiddenException
from app.model.mixin import BaseMixin
from app.model.account.unsigned_student import UnsignedStudentModel


class StudentModel(db.Model, BaseMixin):
    __tablename__ = 'student'
    id = db.Column(db.String, primary_key=True)
    pw = db.Column(db.String)
    name = db.Column(db.String)
    number = db.Column(db.Integer)
    email = db.Column(db.String)

    def __init__(self, id: str, pw: str, name: str, number: int, email: str):
        self.id = id
        self.pw = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt()).decode()
        self.name = name
        self.number = number
        self.email = email

    @staticmethod
    def get_student_by_id(id: str) -> 'StudentModel':
        return StudentModel.query.filter_by(id=id).first()

    @staticmethod
    def get_student_by_id_email(id: str, email:str) -> 'StudentModel':
        student = StudentModel.query.filter_by(id=id, email=email).first()
        if student is None:
            raise ResetContentException()
        return student

    @staticmethod
    def signup(id, pw, unsigned_student: UnsignedStudentModel):
        name = unsigned_student.name
        number = unsigned_student.number
        email = unsigned_student.email

        if StudentModel.get_student_by_id(id) is not None:
            raise ResetContentException()

        StudentModel(id, pw, name, number, email).save()

    @staticmethod
    def login(id: str, pw: str) -> Union[None, 'StudentModel']:
        student: StudentModel = StudentModel.get_student_by_id(id)
        if not student or not bcrypt.checkpw(pw.encode('utf-8'), student.pw.encode('utf-8')):
            raise NoContentException()
        return student

    @staticmethod
    def change_pw(id: str, current_pw: str, new_pw: str):
        student: StudentModel = StudentModel.get_student_by_id(id)
        if student is None:
            raise WrongAuthExcption()

        if not bcrypt.checkpw(current_pw.encode(), student.pw):
            raise ForbiddenException()

        if bcrypt.checkpw(new_pw.encode(), student.pw):
            raise ResetContentException()

        student.pw = bcrypt.hashpw(new_pw.encode(), bcrypt.gensalt()).decode()
        db.session.commit()

    @staticmethod
    def reset_pw(id: str):
        student: StudentModel = StudentModel.get_student_by_id(id)
        student.pw = bcrypt.hashpw('1234'.encode(), bcrypt.gensalt()).decode()
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
