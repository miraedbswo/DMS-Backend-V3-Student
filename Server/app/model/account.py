import bcrypt
import re

from app.extension import db


class StudentModel(db.Model):
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

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_student_by_id(self, id: str):
        return self.query.filter_by(id=id).first()

    def login(self, id: str, pw: str):
        student: StudentModel = self.get_student_by_id(id)
        if not student or not bcrypt.checkpw(pw, student.pw):
            return None
        return student

    def change_pw(self, id: str, current_pw: str, new_pw: str):
        student: StudentModel = self.get_student_by_id(id)
        if bcrypt.checkpw(current_pw, student.pw):
            student.pw = bcrypt.hashpw(new_pw.encode(), bcrypt.gensalt())
            db.session.commit()
            return True
        return False

    def reset_pw(self, id: str):
        student: StudentModel = self.get_student_by_id(id)
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


class UnsignedStudentModel(db.Model):
    __tablename__ = 'unsigned_student_model'
    uuid = db.column(db.String, primary_key=True)
    name = db.column(db.String)
    number = db.column(db.Integer)
    email = db.column(db.String)

    def __init__(self, uuid, name, number, email):
        self.uuid = uuid
        self.name = name
        self.number = number
        self.email = email

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
