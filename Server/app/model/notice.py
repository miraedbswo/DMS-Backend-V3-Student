from datetime import datetime

from app.extension import db
from app.model.mixin import BaseMixin
from app.exception import NoContentException


class NoticeModel(db.Model, BaseMixin):
    __tablename__ = 'notice'

    id: int = db.Column(db.Integer, primary_key=True)
    post_date: datetime = db.Column(db.DateTime)
    title: str = db.Column(db.String)
    content: str = db.Column(db.String)

    def __init__(self, title: str, content: str):
        self.post_date: datetime = datetime.now()
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
                } for notice in NoticeModel.query.all()
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
    title: str = db.Column(db.String)
    content: str = db.Column(db.String)

    def __init__(self, title: str, content: str):
        self.post_date: datetime = datetime.now()
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
