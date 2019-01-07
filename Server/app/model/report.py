from app.extension import db
from app.model.mixin import BaseMixin


class FacilityReport(db.Model, BaseMixin):
    __tablename__ = 'facility_report'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('student_model.id', ondelete='CASCADE'))
    room = db.Column(db.Integer)
    content = db.Column(db.String)

    def __init__(self, student_id, room, content):
        self.student_id = student_id
        self.room = room
        self.content = content

    @db.validates('room')
    def validate_room(self, key, room):
        assert 201 <= room <= 524
        return room
