from app.extension import db
from app.model.mixin import BaseMixin


class PointStatusModel(db.Model, BaseMixin):
    __tablename__ = 'point_status'

    student_id: str = db.Column(db.String, db.ForeignKey('student.id', ondelete='CASCADE'), primary_key=True)
    good_point: int = db.Column(db.Integer, default=0)
    bad_pint: int = db.Column(db.Integer, default=0)
    penalty_level: int = db.Column(db.Integer, default=0)
    penalty_status: bool = db.Column(db.Boolean, default=False)

    def __init__(self, student_id: str):
        self.student_id = student_id

    @staticmethod
    def get_point_status(student_id: str):
        point_status: PointStatusModel = PointStatusModel.query.filter_by(student_id=student_id).first()
        if point_status is None:
            point_status = PointStatusModel(student_id).save()

        return {
            'badPoint': point_status.bad_pint,
            'goodPoint': point_status.good_point,
            'penaltyLevel': point_status.penalty_level,
            'penaltyStatus': point_status.penalty_status
        }
