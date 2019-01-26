from flask import request, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flasgger import swag_from

from app.doc.account.manage import CHANGE_PW_PATCH, FIND_PW_POST
from app.view.base_resource import AccountResource
from app.model import StudentModel


class ManagePasswordView(AccountResource):
    @swag_from(CHANGE_PW_PATCH)
    @jwt_required
    def patch(self):
        id = get_jwt_identity()
        cur_pw = request.json['currentPassword']
        new_pw = request.json['newPassword']

        StudentModel.change_pw(id, cur_pw, new_pw)
        return Response('', 201)

    @swag_from(FIND_PW_POST)
    def post(self):
        id = request.json['id']
        email = request.json['email']
        student = StudentModel.get_student_by_id_email(id, email)

        # TODO: Send Email
        return Response('', 201)
