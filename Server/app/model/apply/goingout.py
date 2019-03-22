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


def str_to_datetime(string) -> dict:
    day = string[:6]
    now = datetime.now()
    year = str(now.year) + '-'

    go_out_date: datetime = datetime.strptime(year + day + string[6:11], '%Y-%m-%d %H:%M')
    return_date: datetime = datetime.strptime(year + day + string[-5:], '%Y-%m-%d %H:%M')

    return {
        'go_out_date': go_out_date,
        'return_date': return_date
    }


def datetime_to_str(go_out_date: datetime, return_date: datetime) -> str:
    go_out_date: str = datetime.strftime(go_out_date, "%m-%d %H:%M")
    return_date: str = datetime.strftime(return_date, "%H:%M")

    return go_out_date + ' ~ ' + return_date


class GoingoutApplyModel(db.Model, BaseMixin):
    __tablename__ = 'goingout'
    id: int = db.Column(db.Integer, primary_key=True)
    student_id: str = db.Column(db.String, db.ForeignKey('student.id', ondelete='CASCADE'))
    go_out_date: datetime = db.Column(db.DateTime)
    return_date: datetime = db.Column(db.DateTime)
    reason: str = db.Column(db.String)
    # 0: 외출 전. 1: 외출 중, 2: 복귀 완료
    goingout_status: int = db.Column(db.Integer, default=0)

    def __init__(self, student_id: str, go_out_date: datetime, return_date: datetime, reason: str):
        self.student_id = student_id
        self.go_out_date = go_out_date
        self.return_date = return_date
        self.reason = reason

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
            days_of_week = apply.go_out_date.weekday()

            date = datetime_to_str(apply.go_out_date, apply.return_date)

            apply = {
                'date': date,
                'id': apply.id,
                'reason': apply.reason,
                'goingoutStatus': goingout_status_message[apply.goingout_status]
            }

            if days_of_week <= 4:
                goingout_data['workday'].append(apply)

            elif days_of_week == 5:
                goingout_data['saturday'].append(apply)

            else:
                goingout_data['sunday'].append(apply)

        return goingout_data

    @staticmethod
    def post_goingout_apply(student_id: str, date: str, reason: str):
        date_dict = str_to_datetime(date)
        go_out_date = date_dict.get('go_out_date')
        return_date = date_dict.get('return_date')

        GoingoutApplyModel(student_id, go_out_date, return_date, reason).save()

    @staticmethod
    def patch_goingout_apply(apply_id: int, student_id: str, date: str, reason: str):
        apply: 'GoingoutApplyModel' = GoingoutApplyModel.query.filter_by(id=apply_id, student_id=student_id).first()
        date_dict = str_to_datetime(date)

        apply.go_out_date = date_dict.get('go_out_date')
        apply.return_date = date_dict.get('return_date')
        apply.reason = reason

        db.session.commit()

    @staticmethod
    def delete_goingout_apply(apply_id: int, student_id: str):
        apply: 'GoingoutApplyModel' = GoingoutApplyModel.query.filter_by(id=apply_id, student_id=student_id).first()

        if apply is None:
            raise NoContentException()
        apply.delete()
