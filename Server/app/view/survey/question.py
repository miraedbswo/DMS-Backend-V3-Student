from flasgger import swag_from
from flask_jwt_extended import jwt_required

from app.doc.survey.question import QUESTION_POST
from app.view.base import SurveyResource


class Question(SurveyResource):
    @swag_from(QUESTION_POST)
    @jwt_required
    def post(self, question_id):
        # TODO: Question View
        pass
