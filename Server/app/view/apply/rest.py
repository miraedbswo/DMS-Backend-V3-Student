import json
from http import HTTPStatus

from flask_jwt_extended import get_jwt_identity, jwt_required

from app.context import context_property
from app.model.apply.rest import RestModel
from app.util.validate import data_type_validate, REST_PATCH_JSON
from app.view.base import ApplyResource


class Rest(ApplyResource):
    @jwt_required
    def get(self):
        student_id = get_jwt_identity()
        rest_status = RestModel.get_apply_by_student_id(student_id)

        return json.dumps(rest_status.__dict__), HTTPStatus.OK

    @data_type_validate(REST_PATCH_JSON)
    @jwt_required
    def patch(self):
        student_id = get_jwt_identity()
        payload = context_property.request_payload

        morning = payload.get('morning')
        afternoon = payload.get('afternoon')

        RestModel.patch_apply(student_id, morning, afternoon)
        return '', HTTPStatus.OK

