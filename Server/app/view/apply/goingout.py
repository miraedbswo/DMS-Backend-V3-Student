from datetime import datetime
from http import HTTPStatus

from flasgger import swag_from
from flask import Response
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.context import context_property
from app.doc.apply.goingout import GOINGOUT_GET, GOINGOUT_POST, GOINGOUT_PATCH, GOINGOUT_DELETE
from app.exception import ApplyTimeException, NotFoundException
from app.model import GoingOutApplyModel
from app.model.apply.goingout import str_to_datetime
from app.util.validate import data_type_validate, GOINGOUT_POST_JSON, GOINGOUT_PATCH_JSON, GOINGOUT_DELETE_JSON
from app.view.base import ApplyResource


class GoingOut(ApplyResource):
    @swag_from(GOINGOUT_GET)
    @jwt_required
    def get(self):
        student_id = get_jwt_identity()
        going_out_applies = GoingOutApplyModel.get_going_out_apply(student_id)

        return going_out_applies, HTTPStatus.OK

    @data_type_validate(GOINGOUT_POST_JSON)
    @swag_from(GOINGOUT_POST)
    @jwt_required
    def post(self):
        student_id = get_jwt_identity()
        payload = context_property.request_payload

        going_out_type = payload.get('type')
        date = payload.get('date')
        place = payload.get('place')

        date_dict = str_to_datetime(date)
        go_out_date: datetime = date_dict.get('go_out_date')
        return_date: datetime = date_dict.get('return_date')

        if not GoingOutApplyModel.verify_apply_time(go_out_date, return_date):
            raise ApplyTimeException()

        GoingOutApplyModel.post_going_out_apply(
            student_id,
            going_out_type,
            go_out_date,
            return_date,
            place,
        )

        return '', HTTPStatus.CREATED


class GoingOutDetail(ApplyResource):
    @data_type_validate(GOINGOUT_PATCH_JSON)
    @swag_from(GOINGOUT_PATCH)
    @jwt_required
    def patch(self, apply_id: int):
        """
        행선지 수정은 언제든 가능하지만, 외출 타입, 시간은 변경 불가능
        """
        student_id = get_jwt_identity()
        payload = context_property.request_payload

        going_out_type = payload.get('type')
        date = payload.get('date')
        place = payload.get('place')

        date_dict = str_to_datetime(date)
        go_out_date: datetime = date_dict.get('go_out_date')
        return_date: datetime = date_dict.get('return_date')

        if not GoingOutApplyModel.verify_apply_time(go_out_date, return_date):
            raise ApplyTimeException()

        GoingOutApplyModel.patch_going_out_apply(apply_id, going_out_type, go_out_date, return_date, place)
        return Response('', 200)

    @data_type_validate(GOINGOUT_DELETE_JSON)
    @swag_from(GOINGOUT_DELETE)
    @jwt_required
    def delete(self, apply_id: int):
        """
        당일날 외출 취소 금지
        """
        student_id = get_jwt_identity()
        apply = GoingOutApplyModel.get_apply_by_id_and_student_id(apply_id, student_id)

        if apply is None:
            raise NotFoundException()

        if not GoingOutApplyModel.verify_apply_time(apply.go_out_date, apply.return_date):
            raise ApplyTimeException()

        GoingOutApplyModel.delete_going_out_apply(apply)

        return Response('', 200)

