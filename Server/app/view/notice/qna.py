from app.doc.notice.qna import QNA_GET, QNA_LIST_GET
from app.view.base_resource import NoticeResource

from flasgger import swag_from


class QnaListView(NoticeResource):
    @swag_from(QNA_LIST_GET)
    def get(self):
        pass


class QnaView(NoticeResource):
    @swag_from(QNA_GET)
    def get(self):
        pass
