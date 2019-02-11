from datetime import datetime
from typing import List

from app.extension import db
from app.exception import NoContentException
from app.model.mixin import BaseMixin


class GoingoutApplyModel(db.Model, BaseMixin):
    __tablename__ = 'goingout'
    id: int = db.Column(db.Integer, primary_key=True)
    student_id: str = db.Column(db.String, db.ForeignKey('student.id', ondelete='CASCADE'))
    go_out_date: datetime = db.Column(db.DateTime)
    return_date: datetime = db.Column(db.DateTime)
    reason: str = db.Column(db.String)

    def __init__(self, student_id: str, go_out_date: datetime, return_date: datetime, reason: str):
        self.student_id = student_id
        self.go_out_date = go_out_date
        self.return_date = return_date
        self.reason = reason

    @staticmethod
    def post_goingout_apply(student_id: str, go_out_date: datetime, return_date: datetime, reason: str):
        GoingoutApplyModel(student_id, go_out_date, return_date, reason).save()

    @staticmethod
    def get_goingout_apply(student_id: str) -> List[dict]:
        applies: List['GoingoutApplyModel'] = GoingoutApplyModel.query.filter_by(student_id=student_id).all()

        if not applies:
            return None

        applies = [
            {
                'goOutDate': str(apply.go_out_date),
                'returnDate': str(apply.return_date),
                'reason': apply.reason
            }
        for apply in applies]

        return applies

    @staticmethod
    def delete_goingout_apply(apply_id: int, student_id: str):
        apply = GoingoutApplyModel.query.filter_by(id=apply_id, student_id=student_id).first()

        if apply is None:
            raise NoContentException()
        apply.delete()
