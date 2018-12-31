from app.extension import db

week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']


class MusicApplyModel(db.Model):
    __tablename__ = 'music_apply_model'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Enum(*week))
    student_id = db.Column(db.String, db.ForeignKey('student_model.id'))
    singer = db.Column(db.String)
    song_name = db.Column(db.String)


class GoingoutApplyModel(db.Model):
    __tablename__ = 'goingout_model'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('student_model.id'))
    go_out_date = db.Column(db.DateTime)
    return_date = db.Column(db.DateTime)
    reason = db.Column(db.String)


class ExtensionApplyModel(db.Model):
    __tablename__ = 'extension_apply_model'
    student_id = db.Column(db.String, db.ForeignKey('student_model.id'), primary_key=True)
    time = db.Column(db.Enum('11', '12'))
    class_ = db.Column(db.Integer)
    seat = db.Column(db.Integer)


class StayApplyModel(db.Model):
    __tablename__ = 'stay_apply_model'
    student_id = db.Column(db.String, db.ForeignKey('student_model.id'), primary_key=True)
    value = db.Column(db.Enum('fri_go', 'sat_go', 'sat_come', 'stay'))
