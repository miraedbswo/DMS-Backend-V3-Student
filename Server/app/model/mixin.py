from datetime import datetime

from pytz import timezone

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
        now = datetime.utcnow()
        KST = timezone('Asia/Seoul')
        return KST.localize(now)
