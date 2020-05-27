from datetime import date as Date
from typing import List

from app.extension import db
from app.model.mixin import BaseMixin

type_list = ['breakfast', 'lunch', 'dinner']


class MealModel(db.Model, BaseMixin):
    __tablename__ = 'meal'
    date: Date = db.Column(db.Date, primary_key=True)
    type: int = db.Column(db.Integer, primary_key=True)  # type (0: 아침, 1: 점심, 2: 저녁)
    meal: str = db.Column(db.String(300))  # ||로 구분하여 입력

    def __init__(self, date: Date, type: int, meal: str):
        self.date = date
        self.type = type
        self.meal = meal

    @staticmethod
    def get_meal(date: Date) -> dict:
        meal_list: List['MealModel'] = MealModel.query.filter_by(date=date).order_by('type')

        return {
            str(date): {
                type_list[meal.type]: meal.meal.split('||')
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
        self.assert_validation(type in [0, 1, 2])
        return type
