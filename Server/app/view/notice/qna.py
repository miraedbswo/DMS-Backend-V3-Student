from flasgger import swag_from
from flask import jsonify

from app.doc.notice.qna import QNA_GET, QNA_LIST_GET
from app.view.base_resource import NoticeResource
from app.model import QNAModel


class QnaListView(NoticeResource):
    @swag_from(QNA_LIST_GET)
    def get(self):
        return jsonify(QNAModel.get_qna_list())


class QnaView(NoticeResource):
    @swag_from(QNA_GET)
    def get(self, qna_id):
        return jsonify(QNAModel.get_qna(qna_id))
