from datetime import date

from app.extension import db
from app.model.mixin import BaseMixin


class PointHistoryModel(db.Model, BaseMixin):
    __tablename__ = 'point_history_model'

    id: int = db.Column(db.Integer, primary_key=True)
    student_id: str = db.Column(db.String, 'student_model.id', ondelete='CASCADE')
    point_id: int = db.Column(db.Integer, db.ForeignKey('point_item_model.id', ondelete='CASCADE'))
    point_date: date = db.Column(db.Date)

    def __init__(self, student_id: str, point_id: int):
        self.student_id: str = student_id
        self.point_id: int = point_id
        self.point_date: date = date.today()

    @staticmethod
    def get_point_history(student_id: str):
        PointHistoryModel.query.filter_by(student_id=student_id).all()
        # TODO: PointItemModel에서 포인트에 대한 정보 가져와 리턴하기
