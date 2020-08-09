from datetime import datetime
from typing import List

from app.exception import ResetContentException, NoContentException, ForbiddenException, AlreadyApplyMusic
from app.extension import db
from app.model import StudentModel
from app.model.base import BaseMixin

week = [0, 1, 2, 3, 4]
weekday = ['mon', 'tue', 'wed', 'thu', 'fri']


class MusicApplyModel(db.Model, BaseMixin):
    __tablename__ = 'music_apply'
    id: int = db.Column(db.Integer, primary_key=True)
    # (0 = 월요일, 1 = 화요일, 2 = 수요일, 3 = 목요일, 4 = 금요일)
    day: int = db.Column(db.Integer)
    student_id: str = db.Column(db.String(20), db.ForeignKey('student.id', ondelete='CASCADE'))
    singer: str = db.Column(db.String(20))
    song_name: str = db.Column(db.String(50))
    apply_date: datetime = db.Column(db.DateTime)

    def __init__(self, day: int, student_id: str, singer: str, song_name: str):
        self.day = day
        self.student_id = student_id
        self.singer = singer
        self.song_name = song_name
        self.apply_date = self.kst_now()

    @staticmethod
    def get_music_apply_by_id(student_id: str):
        return MusicApplyModel.query.filter_by(student_id=student_id).first()

    @staticmethod
    def get_music_apply() -> List['MusicApplyModel']:
        return MusicApplyModel.query.order_by(MusicApplyModel.day, MusicApplyModel.apply_date).all()

    @staticmethod
    def get_music_apply_status() -> dict:
        status = {week: [] for week in weekday}
        music_apply = MusicApplyModel.get_music_apply()

        if not music_apply:
            raise NoContentException()

        if music_apply is not None:
            for apply in music_apply:
                student = StudentModel.get_student_by_id(apply.student_id)
                status[weekday[apply.day]].append(
                    {
                        'id': apply.id,
                        'musicName': apply.song_name,
                        'singer': apply.singer,
                        'studentId': apply.student_id,
                        'applyDate': str(apply.apply_date),
                        'studentName': student.name
                    }
                )

        return status

    @staticmethod
    def post_music_apply(day: int, student_id: str, singer: str, song_name: str):
        if len(MusicApplyModel.query.filter_by(day=day).all()) >= 3:
            raise ResetContentException()

        already_exist_apply = MusicApplyModel.get_music_apply_by_id(student_id)

        if already_exist_apply is not None:
            raise AlreadyApplyMusic()

        MusicApplyModel(day, student_id, singer, song_name).save()

    @staticmethod
    def delete_music_apply(student_id: str, apply_id: int):
        apply: 'MusicApplyModel' = MusicApplyModel.query.filter_by(id=apply_id).first()
        if apply is None:
            raise NoContentException()
        if apply.student_id != student_id:
            raise ForbiddenException()
        apply.delete()

    @db.validates('day')
    def validate_day(self, key, day):
        self.assert_validation(day in week)
        return day
