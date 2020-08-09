from flasgger import swag_from
from flask import jsonify, Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.context import context_property
from app.doc.apply.stay import STAY_GET, STAY_POST
from app.exception import ApplyTimeException
from app.model import StayApplyModel
from app.util.validate import data_type_validate, STAY_POST_JSON
from app.view.base import ApplyResource


class Stay(ApplyResource):
    @swag_from(STAY_GET)
    @jwt_required
    def get(self):
        student_id = get_jwt_identity()
        return jsonify(StayApplyModel.get_stay_apply_status(student_id))

    @data_type_validate(STAY_POST_JSON)
    @swag_from(STAY_POST)
    @jwt_required
    def post(self):
        payload = context_property.request_payload

        apply_time = self.kst_now()
        if (apply_time.weekday() == 3 and apply_time.hour >= 22) or \
                (4 <= apply_time.weekday() <= 5) or \
                (apply_time.weekday() == 6 and apply_time.hour <= 20 and apply_time.minute < 30):
            raise ApplyTimeException()

        student_id = get_jwt_identity()
        value = payload.get('value')

        StayApplyModel.post_stay_apply(student_id, value)
        return Response('', 201)
