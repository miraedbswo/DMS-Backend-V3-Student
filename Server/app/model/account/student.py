import re
from typing import Union

from werkzeug.security import generate_password_hash, check_password_hash

from app.exception import NoContentException, ResetContentException, WrongAuthException, ForbiddenException
from app.extension import db
from app.model.account.unsigned_student import UnsignedStudentModel
from app.model.mixin import BaseMixin


class StudentModel(db.Model, BaseMixin):
    __tablename__ = 'student'
    id: str = db.Column(db.String(20), primary_key=True)
    pw: str = db.Column(db.String(100))
    name: str = db.Column(db.String(20))
    number: int = db.Column(db.Integer)
    email: str = db.Column(db.String(50), nullable=True)

    def __init__(self, id: str, pw: str, name: str, number: int, email: str):
        self.id = id
        self.pw = generate_password_hash(pw)
        self.name = name
        self.number = number
        self.email = email

    @staticmethod
    def get_student_by_id(id: str) -> 'StudentModel':
        return StudentModel.query.filter_by(id=id).first()

    @staticmethod
    def get_student_by_id_email(id: str, email: str) -> 'StudentModel':
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
        unsigned_student.delete()

    @staticmethod
    def login(id: str, pw: str) -> Union[None, 'StudentModel']:
        student: StudentModel = StudentModel.get_student_by_id(id)
        if not student or not check_password_hash(student.pw, pw):
            raise NoContentException()
        return student

    @staticmethod
    def change_pw(id: str, current_pw: str, new_pw: str):
        student: StudentModel = StudentModel.get_student_by_id(id)
        if student is None:
            raise WrongAuthException()

        if not check_password_hash(student.pw, current_pw):
            raise ForbiddenException()

        if check_password_hash(student.pw, new_pw):
            raise ResetContentException()

        student.pw = generate_password_hash(new_pw)
        db.session.commit()

    @staticmethod
    def reset_pw(id: str):
        student: StudentModel = StudentModel.get_student_by_id(id)
        student.pw = generate_password_hash('1234')
        db.session.commit()

    @db.validates('id')
    def validate_id(self, key, id):
        self.assert_validation(4 <= len(id) <= 16)
        return id

    @db.validates('number')
    def validate_pw(self, key, number):
        grade = number // 1000
        class_ = number // 100 % 10
        number_ = number % 100

        self.assert_validation(1 <= grade <= 3 and 1 <= class_ <= 4 and 1 <= number_ <= 21)
        return number

    @db.validates('email')
    def validate_email(self, key, email):
        self.assert_validation(re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@dsm.hs.kr$", email) is not None)
        return email
