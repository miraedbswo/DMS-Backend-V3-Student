from flask import Blueprint
from flask_restful import Api


survey_blueprint = Blueprint('survey', __name__, url_prefix='/survey')
api = Api(survey_blueprint)


from .survey import Survey
api.add_resource(Survey, '/<survey_id>', defaults={'survey_id': None})

from .question import Question
api.add_resource(Question, '/question/<question_id>')
