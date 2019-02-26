from datetime import date as Date
from typing import List

from app.extension import db
from app.model.mixin import BaseMixin

type_list = ['breakfast', 'lunch', 'dinner']


class MealModel(db.Model, BaseMixin):
    __tablename__ = 'meal'
    date: Date = db.Column(db.Date, primary_key=True)
    type: int = db.Column(db.Integer)
    meal: str = db.Column(db.String)  # ||로 구분하여 입력

    def __init__(self, date: Date, type: int, meal: str):
        self.date = date
        self.type = type
        self.meal = meal

    @staticmethod
    def get_meal(date: Date) -> dict:
        meal_list: List['MealModel'] = MealModel.query.filter_by(date=date).order_by('type')

        return {
            str(date): {
                type_list[meal.type]: [menu.split('||') for menu in meal.meal if '||' in menu]
                for meal in meal_list
            }
        }

    @staticmethod
    def save_meal(date: Date, type: int, meal: str):
        meal_data: MealModel = MealModel.query.filter_by(date=date).first()
        if meal_data:
            meal_data.delete()
        MealModel(date, type, meal).save()

    @db.validates('type')
    def validate_type(self, key, type):
        assert type in [1, 2, 3]
        return type
