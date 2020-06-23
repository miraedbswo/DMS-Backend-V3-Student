from datetime import datetime

from sqlalchemy import desc

from app.exception import NoContentException
from app.extension import db
from app.model.mixin import BaseMixin


class NoticeModel(db.Model, BaseMixin):
    __tablename__ = 'notice'

    id: int = db.Column(db.Integer, primary_key=True)
    post_date: datetime = db.Column(db.DateTime)
    title: str = db.Column(db.String(50))
    content: str = db.Column(db.String(2000))

    def __init__(self, title: str, content: str):
        self.post_date: datetime = self.kst_now()
        self.title: str = title
        self.content: str = content

    @staticmethod
    def get_notice_list() -> dict:
        return {
            'noticeList': [
                {
                    'id': notice.id,
                    'postDate': str(notice.post_date),
                    'title': notice.title
                } for notice in NoticeModel.query.order_by(desc(NoticeModel.post_date)).all()
            ]
        }

    @staticmethod
    def get_notice(notice_id) -> dict:
        notice: NoticeModel = NoticeModel.query.filter_by(id=notice_id).first()
        if notice is None:
            raise NoContentException()
        return {
            'content': notice.content,
            'title': notice.title,
            'postDate': str(notice.post_date)
        }


class RuleModel(db.Model, BaseMixin):
    __tablename__ = 'rule'

    id: int = db.Column(db.Integer, primary_key=True)
    post_date: datetime = db.Column(db.DateTime)
    title: str = db.Column(db.String(50))
    content: str = db.Column(db.String(200))

    def __init__(self, title: str, content: str):
        self.post_date: datetime = BaseMixin.kst_now()
        self.title: str = title
        self.content: str = content

    @staticmethod
    def get_rule_list() -> dict:
        return {
            'ruleList': [
                {
                    'id': rule.id,
                    'postDate': str(rule.post_date),
                    'title': rule.title
                } for rule in RuleModel.query.all()
            ]
        }

    @staticmethod
    def get_rule(rule_id) -> dict:
        rule: RuleModel = RuleModel.query.filter_by(id=rule_id).first()
        if rule is None:
            raise NoContentException()
        return {
            'content': rule.content,
            'title': rule.title,
            'postDate': str(rule.post_date)
        }
