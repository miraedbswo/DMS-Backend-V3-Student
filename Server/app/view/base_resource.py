import json
from datetime import datetime, timedelta

from flask import Response
from flask_restful import Resource


# 확장성을 위해 기능별로 BaseResource 생성
class BaseResource(Resource):
    @classmethod
    def unicode_safe_json_dumps(cls, data, status_code=200):
        """
        json 형식에서 utf-8 형식 한글이 깨지는 현상 방지.
        한글을 json 으로 보낼 때 unicode_safe_json_dumps를 사용한다.
        :param data: json type (dict)
        :param status_code: http status code
        """

        return Response(
            json.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8'
        )

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
