from app.extension import db
from app.model.mixin import BaseMixin


class StayApplyModel(db.Model, BaseMixin):
    __tablename__ = 'stay_apply'
    student_id: str = db.Column(db.String, db.ForeignKey('student.id', ondelete='CASCADE'), primary_key=True)
    value: int = db.Column(db.Integer)

    def __init__(self, student_id: str, value: int):
        self.student_id = student_id
        self.value = value

    @staticmethod
    def get_stay_apply_status(student_id: str) -> dict:
        stay: 'StayApplyModel' = StayApplyModel.query.filter_by(student_id=student_id).first()
        if stay is None:
            stay = StayApplyModel(student_id, 4).save()
        return {
            'value': stay.value
        }

    @staticmethod
    def post_stay_apply(student_id: str, value: int):
        stay = StayApplyModel.query.filter(StayApplyModel.student_id == student_id).first()
        if stay:
            stay.delete()

        StayApplyModel(student_id, value).save()

    @db.validates('value')
    def validate_value(self, key, value):
        assert 1 <= value <= 4
        return value
