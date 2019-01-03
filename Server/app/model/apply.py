from app.extension import db

week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']


class MusicApplyModel(db.Model):
    __tablename__ = 'music_apply_model'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Enum(*week))
    student_id = db.Column(db.String, db.ForeignKey('student_model.id', ondelete='CASCADE'))
    singer = db.Column(db.String)
    song_name = db.Column(db.String)

    def __init__(self, day, student_id, singer, song_name):
        self.day = day
        self.student_id = student_id
        self.singer = singer
        self.song_name = song_name


class GoingoutApplyModel(db.Model):
    __tablename__ = 'goingout_model'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('student_model.id', ondelete='CASCADE'))
    go_out_date = db.Column(db.DateTime)
    return_date = db.Column(db.DateTime)
    reason = db.Column(db.String)

    def __init__(self, student_id, go_out_date, return_date, reason):
        self.student_id = student_id
        self.go_out_date = go_out_date
        self.return_date = return_date
        self.reason = reason


class StayApplyModel(db.Model):
    __tablename__ = 'stay_apply_model'
    student_id = db.Column(db.String, db.ForeignKey('student_model.id', ondelete='CASCADE'), primary_key=True)
    value = db.Column(db.Enum('fri_go', 'sat_go', 'sat_come', 'stay'))

    def __init__(self, student_id, value):
        self.student_id = student_id
        self.value = value

    @db.validates('value')
    def validate_value(self, key, value):
        assert 1 <= value <= 4
        return value
