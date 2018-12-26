from flask_restful import Resource


# 확장성을 위해 기능별로 BaseResource 생성
class BaseResource(Resource):
    pass


class AccountResource(BaseResource):
    pass


class ApplyResource(BaseResource):
    pass


class ReportResource(BaseResource):
    pass


class SurveyResource(BaseResource):
    pass
