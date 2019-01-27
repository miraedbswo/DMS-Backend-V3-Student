from datetime import datetime

from flask import request, jsonify, Response
from flasgger import swag_from
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.doc.apply.goingout import GOINGOUT_GET, GOINGOUT_POST, GOINGOUT_DELETE
from app.view.base_resource import ApplyResource
from app.model import GoingoutApplyModel
from app.exception import ApplyTimeException
from app.util.json_schema import json_type_validate, GOINGOUT_DELETE_JSON, GOINGOUT_POST_JSON


class GoingOutView(ApplyResource):
    @swag_from(GOINGOUT_GET)
    @jwt_required
    def get(self):
        studnet_id = get_jwt_identity()
        goingout_applies = GoingoutApplyModel.get_goingout_apply(studnet_id)

        goingout_applies = {
            'goingOut': [
                {
                    "goOutDate": str(apply.go_out_date),
                    "id": apply.id,
                    "reason": apply.reason,
                    "returnDate": str(apply.return_date)
                }
            for apply in goingout_applies]
        }

        return jsonify(goingout_applies)

    @json_type_validate(GOINGOUT_POST_JSON)
    @swag_from(GOINGOUT_POST)
    @jwt_required
    def post(self):
        request_time = datetime.now()
        if not (0 <= request_time.weekday() <= 3 or request_time.weekday() == 4 and request_time.hour <= 21):
            raise ApplyTimeException()
        student_id = get_jwt_identity()
        go_out_date = self.get_datetime(request.json['goOutDate'])
        return_date = self.get_datetime(request.json['returnDate'])
        reason = request.json['reason']

        GoingoutApplyModel.post_goingout_apply(student_id, go_out_date, return_date, reason)
        return Response('', 201)

    @json_type_validate(GOINGOUT_DELETE_JSON)
    @swag_from(GOINGOUT_DELETE)
    @jwt_required
    def delete(self):
        student_id = get_jwt_identity()
        request_time = datetime.now()
        if not (0 <= request_time.weekday() <= 3 or request_time.weekday() == 4 and request_time.hour <= 21):
            raise ApplyTimeException()

        GoingoutApplyModel.delete_goingout_apply(request.json['applyId'], student_id)

        return Response('', 200)

    def get_datetime(self, request_date: str) -> datetime:
        date = request_date.split()[0].split('-')
        time = request_date.split()[1].split(':')
        return datetime(*date, *time)
