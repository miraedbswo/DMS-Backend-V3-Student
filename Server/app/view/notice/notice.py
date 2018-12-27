from app.doc.notice.notice import NOTICE_LIST_GET, NOTICE_GET
from app.view.base_resource import NoticeResource

from flasgger import swag_from


class NoticeListView(NoticeResource):
    @swag_from(NOTICE_LIST_GET)
    def get(self):
        pass


class NoticeView(NoticeResource):
    @swag_from(NOTICE_GET)
    def get(self, notice_id):
        pass
