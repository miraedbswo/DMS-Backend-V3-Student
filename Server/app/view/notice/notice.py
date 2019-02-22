from flasgger import swag_from
from flask import jsonify

from app.doc.notice.notice import NOTICE_LIST_GET, NOTICE_GET
from app.model import NoticeModel
from app.view.base_resource import NoticeResource


class NoticeListView(NoticeResource):
    @swag_from(NOTICE_LIST_GET)
    def get(self):
        return jsonify(NoticeModel.get_notice_list())


class NoticeView(NoticeResource):
    @swag_from(NOTICE_GET)
    def get(self, notice_id):
        return jsonify(NoticeModel.get_notice(notice_id))
