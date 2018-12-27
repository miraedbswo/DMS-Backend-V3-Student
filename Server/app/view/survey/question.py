from app.doc.survey.question import QUESTION_POST
from app.view.base_resource import SurveyResource

from flasgger import swag_from


class QuestionView(SurveyResource):
    @swag_from(QUESTION_POST)
    def post(self, question_id):
        pass
