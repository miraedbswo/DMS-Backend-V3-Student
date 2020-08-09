from dateti me import datetime, timedelta
from typing import List, Optional

from app.extension import db
from app.model.base import BaseMixin


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


class GoingOutApplyModel(db.Model, BaseMixin):
    __tablename__ = 'goingout'
    id: int = db.Column(db.Integer, primary_key=True)
    student_id: str = db.Column(db.String(20), db.ForeignKey('student.id', ondelete='CASCADE'))
    type: int = db.Column(db.Integer)
    going_out_date: datetime = db.Column(db.DateTime)
    return_date: datetime = db.Column(db.DateTime)
    place: str = db.Column(db.String(100))

    def __init__(
            self,
            student_id: str,
            going_out_type: int,
            go_out_date: datetime,
            return_date: datetime,
            place: str
    ):
        self.student_id = student_id
        self.type = going_out_type
        self.go_out_date = go_out_date
        self.return_date = return_date
        self.place = place

    @classmethod
    def get_apply_by_id_and_student_id(cls, id: int, student_id: str) -> Optional['GoingOutApplyModel']:
        return GoingOutApplyModel.query.filter_by(id=id, student_id=student_id).first()

    @staticmethod
    def verify_apply_time(go_out_date: datetime, return_date: datetime) -> bool:
        now = datetime.now()

        if now.date() == go_out_date.date():
            return False

        if (now.weekday() in {4, 5}) and (now.hour >= 22 and now.minute >= 30):
            if now.date() + timedelta(days=1) == go_out_date.date():
                return False

        if go_out_date.date() != return_date.date():
            return False

        difference_time = go_out_date - now
        if not difference_time <= timedelta(days=7):
            return False

        return True

    @staticmethod
    def get_going_out_apply(student_id: str) -> dict:
        applies: List['GoingOutApplyModel'] = GoingOutApplyModel.query.filter(
            GoingOutApplyModel.student_id == student_id,
            GoingOutApplyModel.return_date > datetime.now()
        ).order_by(
            GoingOutApplyModel.updated_at.asc()
        ).all()

        going_out_data = {
            'saturday': [],
            'sunday': []
        }

        for apply in applies:
            days_of_week = apply.go_out_date.weekday()

            apply = {
                'type': apply.type,
                'date': datetime.strftime(apply.go_out_date, "%Y-%m-%d"),
                'place': apply.place
            }

            if days_of_week == 5:
                going_out_data['saturday'].append(apply)

            elif days_of_week == 6:
                going_out_data['sunday'].append(apply)

        return going_out_data

    @staticmethod
    def post_going_out_apply(
            student_id: str,
            going_out_type: int,
            go_out_date: datetime,
            return_date: datetime,
            place: str
    ):
        GoingOutApplyModel(student_id, going_out_type, go_out_date, return_date, place).save()

    @staticmethod
    def patch_going_out_apply(
            apply_id: int,
            student_id: str,
            going_out_type: int,
            go_out_date: datetime,
            return_date: datetime,
            place: str
    ):
        apply = GoingOutApplyModel.get_apply_by_id_and_student_id(apply_id, student_id)

        apply.type = going_out_type
        apply.go_out_date = go_out_date
        apply.return_date = return_date
        apply.place = place

        db.session.commit()

    @staticmethod
    def delete_going_out_apply(apply: 'GoingOutApplyModel'):
        apply.delete()
