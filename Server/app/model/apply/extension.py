from typing import Union

from app.extension import db
from app.exception import NoContentException, ResetContentException
from app.model.mixin import BaseMixin

seat_count = [0, 20, 20, 20, 20, 44, 44, 43, 23]


class ExtensionApplyModel(db.Model, BaseMixin):
    __tablename__ = 'extension_apply'
    student_id = db.Column(db.String, db.ForeignKey('student.id', ondelete='CASCADE'), primary_key=True)
    time = db.Column(db.Integer, primary_key=True)
    class_ = db.Column(db.Integer)
    seat = db.Column(db.Integer)

    def __init__(self, student_id, time, class_, seat):
        self.student_id = student_id
        self.time = time
        self.class_ = class_
        self.seat = seat

    @staticmethod
    def get_extension_apply(student_id: str, time: int) -> 'ExtensionApplyModel':
        return ExtensionApplyModel.query.filter_by(student_id=student_id, time=time).first()

    @staticmethod
    def get_extension_apply_by_seat(class_: int, seat: int) -> 'ExtensionApplyModel':
        return ExtensionApplyModel.query.filter_by(class_=class_, seat=seat).first()

    @staticmethod
    def get_extension_apply_status(student_id: str, time: int) -> Union[None, dict]:
        extension = ExtensionApplyModel.get_extension_apply(student_id, time)
        if extension is None:
            return None
        return {
            'classNum': extension.class_,
            'seatNum': extension.seat
        }

    @staticmethod
    def post_extension_apply(student_id: str, time: int, class_: int, seat: int):
        extension = ExtensionApplyModel.get_extension_apply_by_seat(class_, seat)
        if extension is not None:
            raise ResetContentException()

        extension = ExtensionApplyModel.get_extension_apply(student_id, time)
        if extension is not None:
            extension.delete()

        ExtensionApplyModel(student_id, time, class_, seat).save()

    @staticmethod
    def delete_extension_apply(student_id: str, time: int):
        extension = ExtensionApplyModel.get_extension_apply(student_id, time).first()
        if extension is None:
            raise NoContentException()

        extension.delete()

    @db.validates('time')
    def validate_time(self, key, time):
        assert time in (11, 12)
        return time

    @db.validates('class_')
    def validate_class_(self, key, class_):
        assert 1 <= class_ <= 8
        return class_

    @db.validates('seat')
    def validate_seat(self, key, seat):
        assert 1 <= seat <= seat_count[self.class_]
        return seat
