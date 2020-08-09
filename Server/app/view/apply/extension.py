from datetime import time as Time

from flasgger import swag_from
from flask import jsonify, Response, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.context import context_property
from app.doc.apply.extension import EXTENSION_GET, EXTENSION_POST, EXTENSION_DELETE, EXTENSION_MAP_GET
from app.exception import NoContentException, ApplyTimeException
from app.model import ExtensionApplyModel
from app.util.validate import data_type_validate, EXTENSION_POST_JSON
from app.view.base import ApplyResource

extension_apply_start = {11: Time(17, 30), 12: Time(17, 30)}
extension_apply_end = {11: Time(20, 30), 12: Time(22, 30)}


class Extension(ApplyResource):
    @swag_from(EXTENSION_GET)
    @jwt_required
    def get(self, time: int):
        id: str = get_jwt_identity()

        extension_apply = ExtensionApplyModel.get_extension_apply_status(id, time)
        if extension_apply is None:
            raise NoContentException()

        return jsonify(extension_apply)

    @data_type_validate(EXTENSION_POST_JSON)
    @swag_from(EXTENSION_POST)
    @jwt_required
    def post(self, time):
        if not extension_apply_start[time] <= self.kst_now().time() <= extension_apply_end[time]:
            raise ApplyTimeException()

        id: str = get_jwt_identity()

        payload = context_property.request_payload
        class_num = payload.get('class_num')
        seat_num = payload.get('seat_num')

        ExtensionApplyModel.post_extension_apply(id, time, class_num, seat_num)
        return Response('', 201)

    @swag_from(EXTENSION_DELETE)
    @jwt_required
    def delete(self, time):
        if not extension_apply_start[time] <= self.kst_now().time() <= extension_apply_end[time]:
            raise ApplyTimeException()

        id: str = get_jwt_identity()
        ExtensionApplyModel.delete_extension_apply(id, time)
        return Response('', 200)


class ExtensionMap(ApplyResource):
    @swag_from(EXTENSION_MAP_GET)
    def get(self, class_num, time):
        map_ = ExtensionApplyModel.get_extension_map(class_num, time)
        return jsonify(map_)
