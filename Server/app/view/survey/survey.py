from app.doc.survey.survey import SURVEY_GET
from app.view.base_resource import SurveyResource

from flasgger import swag_from


class SurveyView(SurveyResource):
    @swag_from(SURVEY_GET)
    def get(self):
        pass
