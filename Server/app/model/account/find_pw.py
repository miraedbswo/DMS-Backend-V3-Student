from datetime import datetime
from uuid import uuid4

from app.extension import db
from app.model.account.student import StudentModel
from app.model.mixin import BaseMixin


class FindPWModel(db.Model, BaseMixin):
    __tablename__ = 'find_pw'
    id = db.Column(db.String, primary_key=True, default=str(uuid4()))
    student = db.Column(db.String, db.ForeignKey('student.id', ondelete='CASCADE'))
    date = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, student):
        self.student = student
        self.save()

    @staticmethod
    def check_uuid(uuid: str):
        find_pw = FindPWModel.query.filter_by(id=uuid).first()
        StudentModel.reset_pw(find_pw.student)
