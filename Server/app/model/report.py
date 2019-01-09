from app.extension import db
from app.model.mixin import BaseMixin


class FacilityReport(db.Model, BaseMixin):
    __tablename__ = 'facility_report'
    id: int = db.Column(db.Integer, primary_key=True)
    student_id: str = db.Column(db.String, db.ForeignKey('student.id', ondelete='CASCADE'))
    room: int = db.Column(db.Integer)
    content: str = db.Column(db.String)

    def __init__(self, student_id: str, room: int, content: str):
        self.student_id: str = student_id
        self.room: int = room
        self.content: int = content

    @staticmethod
    def post_facility_report(student_id: str, room: int, content: str):
        FacilityReport(student_id, room, content).save()

    @db.validates('room')
    def validate_room(self, key, room):
        assert 201 <= room <= 518
        return room
