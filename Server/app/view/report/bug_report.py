from datetime import datetime

from flasgger import swag_from
from flask import request, Response
from flask_jwt_extended import get_jwt_identity
from slacker import Slacker

from app.doc.report.bug_report import BUG_REPORT_POST
from app.view.base_resource import ReportResource
from app.model import StudentModel


class BugReportView(ReportResource):
    slack_bot = Slacker('xoxb-324577197473-BWb8rsUFqLezjczj0g6mWn1I')
    PLATFORM_TYPES = {
        1: 'Web',
        2: 'Android',
        3: 'iOS'
    }

    @swag_from(BUG_REPORT_POST)
    def post(self, platform: int):
        student_id = get_jwt_identity()
        student_name = StudentModel.get_student_by_id(student_id).name

        self.slack_bot.chat.post_message(
            channel='#bug-report',
            text='제보자: {}\n제보시간: {}\n플랫폼: {}\n내용: {}'.format(
                student_name,
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                self.PLATFORM_TYPES[int(platform)],
                request.json['content']
            )
        )

        return Response('', 201)
