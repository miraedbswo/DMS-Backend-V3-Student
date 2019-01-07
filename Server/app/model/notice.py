from app.extension import db
from app.model.mixin import BaseMixin


class NoticeModel(db.Model, BaseMixin):
    __tablename__ = 'notice_model'
    id = db.Column(db.Integer, primary_key=True)
    post_date = db.Column(db.DateTime)
    title = db.Column(db.String)
    content = db.Column(db.String)

    def __init__(self, post_date, title, content):
        self.post_date = post_date
        self.title = title
        self.content = content


class RuleModel(db.Model, BaseMixin):
    __tablename__ = 'rule_model'
    id = db.Column(db.Integer, primary_key=True)
    post_date = db.Column(db.DateTime)
    title = db.Column(db.String)
    content = db.Column(db.String)

    def __init__(self, post_date, title, content):
        self.post_date = post_date
        self.title = title
        self.content = content


class QNAModel(db.Model, BaseMixin):
    __tablename__ = 'qna_model'
    id = db.Column(db.Integer, primary_key=True)
    post_date = db.Column(db.DateTime)
    title = db.Column(db.String)
    content = db.Column(db.String)

    def __init__(self, post_date, title, content):
        self.post_date = post_date
        self.title = title
        self.content = content
