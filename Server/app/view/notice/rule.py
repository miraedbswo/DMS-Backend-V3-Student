from app.doc.notice.rule import RULE_LIST_GET, RULE_GET
from app.view.base_resource import NoticeResource

from flasgger import swag_from


class RuleListView(NoticeResource):
    @swag_from(RULE_LIST_GET)
    def get(self):
        pass


class RuleView(NoticeResource):
    @swag_from(RULE_GET)
    def get(self):
        pass
