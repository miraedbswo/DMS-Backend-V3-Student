from flask import Blueprint
from flask_restful import Api


survey_blueprint = Blueprint('survey', __name__, url_prefix='/survey')
api = Api(survey_blueprint)


from .survey import SurveyView, SurveyListView
api.add_resource(SurveyListView, '')
api.add_resource(SurveyView, '/<survey_id>')

from .question import QuestionView
api.add_resource(QuestionView, '/question/<question_id>')
