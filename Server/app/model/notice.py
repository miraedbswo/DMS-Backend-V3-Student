from app.extension import db


class NoticeModel(db.Model):
    __tablename__ = 'notice_model'
    id = db.Column(db.Integer, primary_key=True)
    post_date = db.Column(db.DateTime)
    title = db.Column(db.String)
    content = db.Column(db.String)


class RuleModel(db.Model):
    __tablename__ = 'rule_model'
    id = db.Column(db.Integer, primary_key=True)
    post_date = db.Column(db.DateTime)
    title = db.Column(db.String)
    content = db.Column(db.String)


class QNAModel(db.Model):
    __tablename__ = 'qna_model'
    id = db.Column(db.Integer, primary_key=True)
    post_date = db.Column(db.DateTime)
    title = db.Column(db.String)
    content = db.Column(db.String)
