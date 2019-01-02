from app.extension import db


class FacilityReport(db.Model):
    __tablename__ = 'facility_report'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('student_model.id'))
    room = db.Column(db.Integer)
    content = db.Column(db.String)
