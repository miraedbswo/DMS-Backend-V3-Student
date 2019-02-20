from flask import Blueprint
from flask_restful import Api


notice_blueprint = Blueprint('notice', __name__)
api = Api(notice_blueprint)

from .notice import NoticeListView, NoticeView
api.add_resource(NoticeListView, '/notice')
api.add_resource(NoticeView, '/notice/<notice_id>')

from .rule import RuleListView, RuleView
api.add_resource(RuleListView, '/rule')
api.add_resource(RuleView, '/rule/<rule_id>')
