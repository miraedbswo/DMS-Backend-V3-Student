from app.extension import db


class StudentModel(db.Model):
    __tablename__ = 'student_model'
    id = db.column(db.String, primary_key=True)
    pw = db.column(db.String)
    name = db.column(db.String)
    number = db.column(db.Integer)
    email = db.column(db.String)


class UnsignedStudentModel(db.Model):
    __tablename__ = 'unsigned_student_model'
    uuid = db.column(db.String, primary_key=True)
    name = db.column(db.String)
    number = db.column(db.Integer)
    email = db.column(db.String)
