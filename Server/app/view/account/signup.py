from flask import request
from flasgger import swag_from

from app.doc.account.signup import SIGNUP_POST
from app.view.base_resource import AccountResource
from app.model import UnsignedStudentModel, StudentModel


class SignupView(AccountResource):
    @swag_from(SIGNUP_POST)
    def post(self):
        uuid = request.json['uuid']
        unsigned_student = UnsignedStudentModel.get_unsigned_student(uuid)

        id = request.json['id']
        pw = request.json['password']
        StudentModel.signup(id, pw, unsigned_student)
        unsigned_student.delete()
