from flask import Blueprint
from flask_restful import Api

notice_blueprint = Blueprint('notice', __name__)
api = Api(notice_blueprint)

from .notice import NoticeList, Notice

api.add_resource(NoticeList, '/notice')
api.add_resource(Notice, '/notice/<notice_id>')

from .rule import RuleList, Rule

api.add_resource(RuleList, '/rule')
api.add_resource(Rule, '/rule/<rule_id>')
