from datetime import date

from flask import jsonify
from flasgger import swag_from

from app.doc.meal.meal import MEAL_GET
from app.view.base_resource import BaseResource
from app.model import MealModel


class MealView(BaseResource):
    @swag_from(MEAL_GET)
    def get(self, day: str):
        meal = MealModel.get_meal(date(*day.split('-')))

        return jsonify(meal)
