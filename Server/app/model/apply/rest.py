from datetime import datetime
from typing import Optional

from app.extension import db
from app.model.base import BaseMixin


class RestModel(db.Model, BaseMixin):
    __tablename__ = 'rest'
    id: int = db.Column(db.Integer, primary_key=True)
    student_id: str = db.Column(db.String(20), db.ForeignKey('student.id', ondelete='CASCADE'), primary_key=True)
    morning: bool = db.Column(db.Boolean, default=False)
    afternoon: bool = db.Column(db.Boolean, default=False)

    def __init__(self, student_id: str, morning: bool, afternoon: bool):
        self.student_id = student_id
        self.morning = morning
        self.afternoon = afternoon

    @classmethod
    def get_apply_by_student_id(cls, student_id: str) -> 'RestModel':
        return RestModel.query.filter_by(student_id=student_id).first()

    @staticmethod
    def post_apply(
            student_id: str,
            morning: bool,
            afternoon: bool
    ):
        RestModel(student_id, morning, afternoon).save()

    @staticmethod
    def patch_apply(
            student_id: str,
            morning: bool,
            afternoon: bool
    ):
        apply = RestModel.get_apply_by_student_id(student_id)

        apply.morning = morning
        apply.afternoon = afternoon

        db.session.commit()
