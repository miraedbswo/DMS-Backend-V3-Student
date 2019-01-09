from datetime import datetime
from typing import List

from app.extension import db
from app.exception import ResetContentException
from app.model.mixin import BaseMixin

week = [0, 1, 2, 3, 4]
weekday = ['mon', 'tue', 'wed', 'thu', 'fri']


class MusicApplyModel(db.Model):
    __tablename__ = 'music_apply'
    id: int = db.Column(db.Integer, primary_key=True)
    # (0 = 월요일, 1 = 화요일, 2 = 수요일, 3 = 목요일, 4 = 금요일)
    day: int = db.Column(db.Integer)
    student_id: str = db.Column(db.String, db.ForeignKey('student.id', ondelete='CASCADE'))
    singer: str = db.Column(db.String)
    song_name: str = db.Column(db.String)
    apply_date: datetime = db.Column(db.DateTime)

    def __init__(self, day: int, student_id: str, singer: str, song_name: str):
        self.day = day
        self.student_id = student_id
        self.singer = singer
        self.song_name = song_name
        self.apply_date = datetime.now()

    @staticmethod
    def get_music_apply() -> List['MusicApplyModel']:
        return MusicApplyModel.query.all().order_by(MusicApplyModel.day, MusicApplyModel.apply_date)

    @staticmethod
    def get_music_apply_status() -> dict:
        status = {week: [] for week in weekday}
        music_apply = MusicApplyModel.get_music_apply()

        if music_apply is not None:
            for apply in music_apply:
                status[weekday[apply.day]].append(
                    [
                        {
                            'id': MusicApplyModel.id,
                            'musicName': MusicApplyModel.song_name,
                            'singer': MusicApplyModel.singer,
                            'studentId': MusicApplyModel.student_id,
                            'applyDate': str(MusicApplyModel.apply_date)
                        }
                    ]
                )

        return status

    @staticmethod
    def post_music_apply(day: int, student_id: str, singer: str, song_name: str):
        if len(MusicApplyModel.query.filter_by(day=day).all()) > 5:
            raise ResetContentException()
        MusicApplyModel(day, student_id, singer, song_name).save()

    @db.validates('day')
    def validate_day(self, key, day):
        assert day in week
        return day
