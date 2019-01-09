from flask import jsonify
from flasgger import swag_from
from flask_jwt_extended import get_jwt_identity

from app.doc.account.info import EXTENSION_INFO_GET, BASIC_INFO_GET, POINT_HISTORY_GET
from app.view.base_resource import AccountResource
from app.model import PointStatusModel, StudentModel


class ExtensionInfoView(AccountResource):
    @swag_from(EXTENSION_INFO_GET)
    def get(self):
        pass


class BasicInfoView(AccountResource):
    @swag_from(BASIC_INFO_GET)
    def get(self):
        id = get_jwt_identity()
        student = StudentModel.get_student_by_id(id)
        info = PointStatusModel.get_point_status(id)

        info['number'] = student.number
        info['name'] = student.name

        return jsonify(info)



class PointInfoView(AccountResource):
    @swag_from(POINT_HISTORY_GET)
    def get(self):
        pass
