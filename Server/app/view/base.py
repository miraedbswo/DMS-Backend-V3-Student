import json
from datetime import datetime, timedelta

from flask import Response
from flask_restful import Resource


# 확장성을 위해 기능별로 BaseResource 생성
class BaseResource(Resource):
    @staticmethod
    def kst_now():
        return datetime.utcnow() + timedelta(hours=9)


class AccountResource(BaseResource):
    pass


class ApplyResource(BaseResource):
    pass


class NoticeResource(BaseResource):
    pass


class ReportResource(BaseResource):
    pass


class SurveyResource(BaseResource):
    pass
