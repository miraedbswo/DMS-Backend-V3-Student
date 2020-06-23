from flasgger import swag_from
from flask import request, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from slacker import Slacker

from app.doc.report.bug_report import BUG_REPORT_POST
from app.model import StudentModel
from app.util.json_schema import json_type_validate, BUG_POST_JSON
from app.view.base_resource import ReportResource


class BugReport(ReportResource):
    slack_bot = Slacker('xoxb-323597966326-1158056204727-dNnaFC2q10RAv9fJG0aChVvd')
    PLATFORM_TYPES = {
        1: 'Web',
        2: 'Android',
        3: 'iOS'
    }

    @json_type_validate(BUG_POST_JSON)
    @swag_from(BUG_REPORT_POST)
    @jwt_required
    def post(self, platform: int):
        student_id = get_jwt_identity()
        student_name = StudentModel.get_student_by_id(student_id).name

        self.slack_bot.chat.post_message(
            channel='#bug-report',
            text='제보자: {}\n제보시간: {}\n플랫폼: {}\n내용: {}'.format(
                student_name,
                self.kst_now().strftime('%Y-%m-%d %H:%M:%S'),
                self.PLATFORM_TYPES[int(platform)],
                request.json['content']
            )
        )

        return Response('', 201)
