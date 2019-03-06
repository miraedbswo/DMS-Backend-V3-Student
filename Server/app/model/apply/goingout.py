from datetime import datetime
from typing import List

from app.exception import NoContentException
from app.extension import db
from app.model.mixin import BaseMixin

goingout_status_message = [
    '외출 전',
    '외출 중',
    '복귀'
]


class GoingoutApplyModel(db.Model, BaseMixin):
    __tablename__ = 'goingout'
    id: int = db.Column(db.Integer, primary_key=True)
    student_id: str = db.Column(db.String, db.ForeignKey('student.id', ondelete='CASCADE'))
    go_out_date: datetime = db.Column(db.DateTime)
    return_date: datetime = db.Column(db.DateTime)
    reason: str = db.Column(db.String)
    # 0: 외출 전. 1: 외출 중, 2: 복귀 완
    goingout_status: int = db.Column(db.Integer, default=0)

    def __init__(self, student_id: str, go_out_date: datetime, return_date: datetime, reason: str):
        self.student_id = student_id
        self.go_out_date = go_out_date
        self.return_date = return_date
        self.reason = reason

    @staticmethod
    def post_goingout_apply(student_id: str, go_out_date: datetime, return_date: datetime, reason: str):
        GoingoutApplyModel(student_id, go_out_date, return_date, reason).save()

    @staticmethod
    def get_goingout_apply(student_id: str) -> dict:
        applies: List['GoingoutApplyModel'] = GoingoutApplyModel.query.filter_by(student_id=student_id).all()

        if not applies:
            raise NoContentException

        goingout_data = {
            'workday': [],
            'saturday': [],
            'sunday': []
        }

        for apply in applies:
            date = apply.go_out_date.weekday()

            apply = {
                'go_out_date': datetime.strftime(apply.go_out_date, "%Y-%m-%d %H:%M"),
                'id': apply.id,
                'return_date': datetime.strftime(apply.return_date, "%Y-%m-%d %H:%M"),
                'reason': apply.reason,
                'goingout_status': goingout_status_message[apply.goingout_status]
            }

            if date <= 4:
                goingout_data['workday'].append(apply)

            elif date == 5:
                goingout_data['saturday'].append(apply)

            else:
                goingout_data['sunday'].append(apply)

        return goingout_data

    @staticmethod
    def delete_goingout_apply(apply_id: int, student_id: str):
        apply = GoingoutApplyModel.query.filter_by(id=apply_id, student_id=student_id).first()

        if apply is None:
            raise NoContentException()
        apply.delete()
