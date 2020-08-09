from datetime import datetime

from flasgger import swag_from
from flask import jsonify

from app.doc.meal.meal import MEAL_GET
from app.model import MealModel
from app.view.base import BaseResource


class Meal(BaseResource):
    @swag_from(MEAL_GET)
    def get(self, day: str):
        try:
            meal = MealModel.get_meal(datetime.strptime(day, '%Y-%m-%d').date())
        except ValueError:
            return '', 205

        return jsonify(meal)
