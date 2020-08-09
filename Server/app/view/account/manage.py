import smtplib
from email.mime.text import MIMEText

from flasgger import swag_from
from flask import request, Response, current_app
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.context import context_property
from app.doc.account.manage import CHANGE_PW_PATCH, FIND_PW_POST
from app.model import StudentModel, FindPWModel
from app.util.validate import data_type_validate, PW_PATCH_JSON, PW_POST_JSON
from app.view.base import AccountResource


class ManagePassword(AccountResource):
    @data_type_validate(PW_PATCH_JSON)
    @swag_from(CHANGE_PW_PATCH)
    @jwt_required
    def patch(self):
        payload = context_property.request_payload
        id = get_jwt_identity()

        cur_pw = payload.get('currentPassword')
        new_pw = payload.get('newPassword')

        StudentModel.change_pw(id, cur_pw, new_pw)
        return Response('', 201)

    @data_type_validate(PW_POST_JSON)
    @swag_from(FIND_PW_POST)
    def post(self):
        payload = context_property.request_payload

        id = payload.get('id')
        email = payload.get('email')
        student = StudentModel.get_student_by_id_email(id, email)

        find_pw = FindPWModel(student=student.id)

        mail_id = current_app.config['MAIL_ID']
        mail_pw = current_app.config['MAIL_PW']

        smtp = smtplib.SMTP(current_app.config['MAIL_SERVER'], current_app.config['MAIL_PORT'])
        smtp.starttls()
        smtp.login(mail_id, mail_pw)

        msg = MIMEText(f'http://dms.istruly.sexy/account/pw/{find_pw.id}')
        msg['Subject'] = 'dms 비밀번호 초기화 링크'
        msg['To'] = 'miraedbswo@gmail.com'
        msg['From'] = mail_id

        smtp.sendmail(mail_id, 'miraedbswo@gmail.com', bytes(msg))

        return Response('', 201)


class FindPWGet(AccountResource):
    def get(self, uuid: str):
        FindPWModel.check_uuid(uuid=uuid)

        return Response('', 200)
