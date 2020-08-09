from flasgger import swag_from
from flask import request, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from slacker import Slacker

from app.context import context_property
from app.doc.report.bug_report import BUG_REPORT_POST
from app.model import StudentModel
from app.util.validate import data_type_validate, BUG_POST_JSON
from app.view.base import ReportResource


class BugReport(ReportResource):
    slack_bot = Slacker('xoxb-324577197473-BWb8rsUFqLezjczj0g6mWn1I')
    PLATFORM_TYPES = {
        1: 'Web',
        2: 'Android',
        3: 'iOS'
    }

    @data_type_validate(BUG_POST_JSON)
    @swag_from(BUG_REPORT_POST)
    @jwt_required
    def post(self, platform: int):
        payload = context_property.request_payload
        student_id = get_jwt_identity()
        student_name = StudentModel.get_student_by_id(student_id).name

        self.slack_bot.chat.post_message(
            channel='#bug-report',
            text='제보자: {}\n제보시간: {}\n플랫폼: {}\n내용: {}'.format(
                student_name,
                self.kst_now().strftime('%Y-%m-%d %H:%M:%S'),
                self.PLATFORM_TYPES[int(platform)],
                payload.get('content')
            )
        )

        return Response('', 201)
