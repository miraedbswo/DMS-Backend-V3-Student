from flasgger import swag_from
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.doc.account.info import APPLY_INFO_GET, BASIC_INFO_GET, POINT_HISTORY_GET
from app.model import (StudentModel, PointStatusModel, ExtensionApplyModel,
                       GoingOutApplyModel, StayApplyModel, PointHistoryModel)
from app.view.base import AccountResource


class ApplyInfo(AccountResource):
    @swag_from(APPLY_INFO_GET)
    @jwt_required
    def get(self):
        student_id = get_jwt_identity()

        apply_info = dict(
            extension11=ExtensionApplyModel.get_extension_apply_status(student_id, 11),
            extension12=ExtensionApplyModel.get_extension_apply_status(student_id, 12),
            goingOut=GoingOutApplyModel.get_going_out_apply(student_id),
            stay=StayApplyModel.get_stay_apply_status(student_id)['value']
        )
        return jsonify(apply_info)


class BasicInfo(AccountResource):
    @swag_from(BASIC_INFO_GET)
    @jwt_required
    def get(self):
        id = get_jwt_identity()
        student = StudentModel.get_student_by_id(id)
        info = PointStatusModel.get_point_status(id)

        info['number'] = student.number
        info['name'] = student.name

        return jsonify(info)


class PointInfo(AccountResource):
    @swag_from(POINT_HISTORY_GET)
    @jwt_required
    def get(self):
        student_id = get_jwt_identity()

        return jsonify(PointHistoryModel.get_point_history(student_id))
