from app.extension import db
from app.model.mixin import BaseMixin


class PointStatusModel(db.Model, BaseMixin):
    __tablename__ = 'point_status_model'

    student_id: str = db.Column(db.String, primary_key=True)
    good_point: int = db.Column(db.Integer, default=0)
    bad_pint: int = db.Column(db.Integer, default=0)
    penalty_level: int = db.Column(db.Integer, default=0)
    penalty_status: bool = db.Column(db.Boolean, default=False)

    def __init__(self, student_id: str):
        self.student_id = student_id

    @staticmethod
    def get_point_status(student_id: str):
        return PointStatusModel.query.filter_by(student_id=student_id).first()
