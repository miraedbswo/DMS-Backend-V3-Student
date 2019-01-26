from datetime import datetime

from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, Response, request

from app.doc.apply.stay import STAY_GET, STAY_POST
from app.view.base_resource import ApplyResource
from app.model import StayApplyModel
from app.exception import ApplyTimeException


class StayView(ApplyResource):
    @swag_from(STAY_GET)
    @jwt_required
    def get(self):
        student_id = get_jwt_identity()
        return jsonify(StayApplyModel.get_stay_apply_status(student_id))

    @swag_from(STAY_POST)
    @jwt_required
    def post(self):
        apply_time = datetime.now()
        if (apply_time.weekday() == 3 and apply_time.hour >= 22) or \
            (4 <= apply_time.weekday() <= 5) or \
            (apply_time.weekday() == 6 and apply_time.hour <= 20 and apply_time.minute < 30):
            raise ApplyTimeException()

        studnet_id = get_jwt_identity()
        value = request.json['value']

        StayApplyModel.post_stay_apply(studnet_id, value)
        return Response('', 201)
