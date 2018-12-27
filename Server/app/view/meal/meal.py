from app.doc.meal.meal import MEAL_GET
from app.view.base_resource import BaseResource

from flasgger import swag_from


class MealView(BaseResource):
    @swag_from(MEAL_GET)
    def get(self):
        pass
