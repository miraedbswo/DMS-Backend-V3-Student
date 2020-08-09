from datetime import datetime
from http import HTTPStatus

from flasgger import swag_from
from flask import jsonify

from app.doc.meal.meal import MEAL_GET
from app.model import MealModel
from app.model.meal import type_list
from app.view.base_resource import BaseResource


class Meal(BaseResource):
    @swag_from(MEAL_GET)
    def get(self, day: str):
        try:
            date = datetime.strptime(day, '%Y-%m-%d').date()
        except ValueError:
            return '', 205

        meals = MealModel.get_meal(date)

        return {
            type_list[meal.type]: meal.meal.split('||')
            for meal in meals
        }, HTTPStatus.OK
