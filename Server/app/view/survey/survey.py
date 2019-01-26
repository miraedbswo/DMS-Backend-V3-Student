from flasgger import swag_from
from flask_jwt_extended import jwt_required

from app.doc.survey.survey import SURVEY_LIST_GET, SURVEY_GET
from app.view.base_resource import SurveyResource


class SurveyListView(SurveyResource):
    @swag_from(SURVEY_LIST_GET)
    @jwt_required
    def get(self):
        # TODO: Survey List View
        pass


class SurveyView(SurveyResource):
    @swag_from(SURVEY_GET)
    @jwt_required
    def get(self):
        # TODO: Survey View
        pass
