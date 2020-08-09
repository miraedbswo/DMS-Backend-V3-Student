from flasgger import swag_from
from flask import request, Response

from app.context import context_property
from app.doc.account.signup import SIGNUP_POST
from app.model import UnsignedStudentModel, StudentModel, PointStatusModel
from app.util.validate import data_type_validate, SIGNUP_POST_JSON
from app.view.base_resource import AccountResource


class Signup(AccountResource):
    @data_type_validate(SIGNUP_POST_JSON)
    @swag_from(SIGNUP_POST)
    def post(self):
        uuid = request.json['uuid']
        payload = context_property.request_payload
        uuid = payload.get('uuid')
        unsigned_student = UnsignedStudentModel.get_unsigned_student(uuid)

        id = payload.get('id')
        pw = payload.get('password')

        StudentModel.signup(id, pw, unsigned_student)
        PointStatusModel(id).save()

        return Response('', 201)
