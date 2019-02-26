from flasgger import swag_from
from flask import jsonify

from app.doc.notice.rule import RULE_LIST_GET, RULE_GET
from app.model import RuleModel
from app.view.base_resource import NoticeResource


class RuleListView(NoticeResource):
    @swag_from(RULE_LIST_GET)
    def get(self):
        return jsonify(RuleModel.get_rule_list())


class RuleView(NoticeResource):
    @swag_from(RULE_GET)
    def get(self, rule_id):
        return jsonify(RuleModel.get_rule(rule_id))
