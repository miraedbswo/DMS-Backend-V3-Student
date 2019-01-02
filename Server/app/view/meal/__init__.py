from flask import Blueprint
from flask_restful import Api


meal_blueprint = Blueprint('meal', __name__)
api = Api(meal_blueprint)


from .meal import MealView
api.add_resource(MealView, '/meal')