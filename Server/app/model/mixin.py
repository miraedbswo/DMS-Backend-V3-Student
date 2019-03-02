from datetime import datetime, timedelta

from app.extension import db


class BaseMixin:

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def kst_now():
        return datetime.utcnow() + timedelta(hours=9)
