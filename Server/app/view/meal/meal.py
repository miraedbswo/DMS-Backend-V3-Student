from datetime import datetime
from http import HTTPStatus

from flasgger import swag_from

from app.doc.meal.meal import MEAL_GET
from app.exception import BadRequestException
from app.model import MealModel
from app.model.meal import type_list
from app.view.base import BaseResource


class Meal(BaseResource):
    @swag_from(MEAL_GET)
    def get(self, day: str):
        try:
            date = datetime.strptime(day, '%Y-%m-%d')
        except ValueError:
            raise BadRequestException()

        meals = MealModel.get_meal_by_date(date)

        return {
            meal_type: meals[idx].menu.split('||')
            for idx, meal_type in enumerate(type_list)
        }, HTTPStatus.OK
