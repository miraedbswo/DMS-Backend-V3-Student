from typing import Union

from app.exception import NoContentException, ResetContentException
from app.extension import db
from app.model.account.student import StudentModel
from app.model.mixin import BaseMixin
from app.util.extension_map import *

seat_count = [0, 20, 20, 20, 20, 23, 24, 20, 24, 20, 49, 8]


class ExtensionApplyModel(db.Model, BaseMixin):
    __tablename__ = 'extension_apply'
    student_id = db.Column(db.String(20), db.ForeignKey('student.id', ondelete='CASCADE'), primary_key=True)
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
    def get_extension_apply_by_seat(class_: int, seat: int, time: int) -> 'ExtensionApplyModel':
        return ExtensionApplyModel.query.filter_by(class_=class_, seat=seat, time=time).first()

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
    def get_extension_apply_by_class_num(class_: int, time: int) -> dict:
        extension_list = ExtensionApplyModel.query.filter_by(class_=class_, time=time).all()

        extension_dict = {
            apply.seat: StudentModel.get_student_by_id(apply.student_id).name
            for apply in extension_list
        }

        return extension_dict

    @staticmethod
    def post_extension_apply(student_id: str, time: int, class_: int, seat: int):
        extension = ExtensionApplyModel.get_extension_apply_by_seat(class_, seat, time)
        if extension is not None:
            raise ResetContentException()

        extension = ExtensionApplyModel.get_extension_apply(student_id, time)
        if extension is not None:
            extension.delete()

        ExtensionApplyModel(student_id, time, class_, seat).save()

    @staticmethod
    def delete_extension_apply(student_id: str, time: int):
        extension = ExtensionApplyModel.get_extension_apply(student_id, time)
        if extension is None:
            raise NoContentException()

        extension.delete()

    @staticmethod
    def get_extension_map(class_num: int, time: int) -> dict:
        apply_list = ExtensionApplyModel.get_extension_apply_by_class_num(class_num, time)
        seat_count = 1

        chart = get_map_chart(class_num)

        for i, row in enumerate(chart):
            for j, seat in enumerate(row):
                if seat:
                    if seat == -1:
                        chart[i][j] = seat
                        continue

                    apply = apply_list.get(seat_count, False)
                    if apply:
                        chart[i][j] = apply
                    else:
                        chart[i][j] = seat_count

                    seat_count += 1

        return {'map': chart}

    @db.validates('time')
    def validate_time(self, key, time):
        self.assert_validation(time in (11, 12))
        return time

    @db.validates('class_')
    def validate_class_(self, key, class_):
        self.assert_validation(1 <= class_ <= 11)
        return class_

    @db.validates('seat')
    def validate_seat(self, key, seat):
        self.assert_validation(1 <= seat <= seat_count[self.class_])
        return seat
