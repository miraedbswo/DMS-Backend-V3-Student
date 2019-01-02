from app.extension import db
import re


class StudentModel(db.Model):
    __tablename__ = 'student_model'
    id = db.column(db.String, primary_key=True)
    pw = db.column(db.String)
    name = db.column(db.String)
    number = db.column(db.Integer)
    email = db.column(db.String)

    def __init__(self, id, pw, name, number, email):
        self.id = id
        self.pw = pw
        self.name = name
        self.number = number
        self.email = email

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
