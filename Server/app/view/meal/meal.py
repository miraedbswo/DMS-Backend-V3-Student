from datetime import datetime

from flask import jsonify
from flasgger import swag_from

from app.doc.meal.meal import MEAL_GET
from app.view.base_resource import BaseResource
from app.model import MealModel


class MealView(BaseResource):
    @swag_from(MEAL_GET)
    def get(self, day: str):
        try:
            meal = MealModel.get_meal(datetime.strptime(day, '%Y-%m-%d').date())
        except ValueError:
            return '', 205

        return jsonify(meal)
