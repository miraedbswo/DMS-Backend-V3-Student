from datetime import date
from typing import List

from app.extension import db
from app.model.mixin import BaseMixin
from app.model.point.item import PointItemModel


class PointHistoryModel(db.Model, BaseMixin):
    __tablename__ = 'point_history'

    id: int = db.Column(db.Integer, primary_key=True)
    student_id: str = db.Column(db.String, 'student.id', ondelete='CASCADE')
    point_id: int = db.Column(db.Integer, db.ForeignKey('point_item.id', ondelete='CASCADE'))
    point_date: date = db.Column(db.Date)

    def __init__(self, student_id: str, point_id: int):
        self.student_id: str = student_id
        self.point_id: int = point_id
        self.point_date: date = date.today()

    @staticmethod
    def get_point_history(student_id: str):
        histories: List['PointHistoryModel'] = PointHistoryModel.query.filter_by(student_id=student_id).all()

        result = {'point_history': []}
        for history in histories:
            temp = PointItemModel.get_point_item(history.point_id)
            temp['date'] = str(history.point_date)
            result['point_history'].append(temp)

        return result
