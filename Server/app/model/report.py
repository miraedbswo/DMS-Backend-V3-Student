from app.extension import db


class FacilityReport(db.Model):
    __tablename__ = 'facility_report'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('student_model.id', ondelete='CASCADE'))
    room = db.Column(db.Integer)
    content = db.Column(db.String)

    def __init__(self, student_id, room, content):
        self.student_id = student_id
        self.room = room
        self.content = content
