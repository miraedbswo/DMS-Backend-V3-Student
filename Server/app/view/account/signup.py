from flasgger import swag_from
from flask import request, Response

from app.doc.account.signup import SIGNUP_POST
from app.model import UnsignedStudentModel, StudentModel, PointStatusModel
from app.util.json_schema import json_type_validate, SIGNUP_POST_JSON
from app.view.base_resource import AccountResource


class Signup(AccountResource):
    @json_type_validate(SIGNUP_POST_JSON)
    @swag_from(SIGNUP_POST)
    def post(self):
        uuid = request.json['uuid']
        unsigned_student = UnsignedStudentModel.get_unsigned_student(uuid)

        id = request.json['id']
        pw = request.json['password']

        StudentModel.signup(id, pw, unsigned_student)
        PointStatusModel(id).save()

        return Response('', 201)
