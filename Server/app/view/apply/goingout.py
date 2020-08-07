from datetime import datetime

from flasgger import swag_from
from flask import request, jsonify, Response
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.doc.apply.goingout import GOINGOUT_GET, GOINGOUT_POST, GOINGOUT_PATCH, GOINGOUT_DELETE
from app.exception import ApplyTimeException
from app.model import GoingOutApplyModel
from app.util.validate import data_type_validate, GOINGOUT_POST_JSON, GOINGOUT_PATCH_JSON, GOINGOUT_DELETE_JSON
from app.view.base_resource import ApplyResource


class GoingOut(ApplyResource):
    @swag_from(GOINGOUT_GET)
    @jwt_required
    def get(self):
        student_id = get_jwt_identity()
        going_out_applies = GoingOutApplyModel.get_going_out_apply(student_id)

        return jsonify(going_out_applies)

    @data_type_validate(GOINGOUT_POST_JSON)
    @swag_from(GOINGOUT_POST)
    @jwt_required
    def post(self):
        student_id = get_jwt_identity()
        date = request.json['date']
        reason = request.json['reason']

        GoingOutApplyModel.post_going_out_apply(student_id, date, reason)
        return Response('', 201)

    @data_type_validate(GOINGOUT_PATCH_JSON)
    @swag_from(GOINGOUT_PATCH)
    @jwt_required
    def patch(self):
        request_time = self.kst_now()
        date = request.json['date']
        go_out_date = datetime.strptime(date[:11], '%m-%d %H:%M')

        if request_time.weekday() == go_out_date.weekday():
            raise ApplyTimeException()

        if not (request_time.weekday() <= 4 or request_time.hour <= 21):
            raise ApplyTimeException()

        apply_id = request.json['applyId']
        reason = request.json['reason']
        student_id = get_jwt_identity()

        GoingOutApplyModel.patch_going_out_apply(apply_id, student_id, date, reason)
        return Response('', 201)

    @data_type_validate(GOINGOUT_DELETE_JSON)
    @swag_from(GOINGOUT_DELETE)
    @jwt_required
    def delete(self):
        student_id = get_jwt_identity()
        request_time = self.kst_now()
        if not (request_time.weekday() <= 4 or request_time.hour <= 21):
            raise ApplyTimeException()

        apply_id = request.json['applyId']

        GoingOutApplyModel.delete_going_out_apply(apply_id, student_id)

        return Response('', 200)

    # def get_datetime(self, request_date: str) -> datetime:
    #     date = map(int, request_date.split()[0].split('-'))
    #     time = map(int, request_date.split()[1].split(':'))
    #     return datetime(*date, *time)
