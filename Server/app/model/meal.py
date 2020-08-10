from datetime import datetime
from typing import List

from app.extension import db
from app.model.base import BaseMixin

type_list = ['breakfast', 'lunch', 'dinner']


class MealModel(db.Model, BaseMixin):
    __tablename__ = 'meal'
    date: datetime = db.Column(db.Date, primary_key=True)
    type: int = db.Column(db.Integer, primary_key=True)  # type (0: 아침, 1: 점심, 2: 저녁)
    menu: str = db.Column(db.String(300))  # ||로 구분하여 입력

    def __init__(self, date: datetime, type: int, menu: str):
        self.date = date
        self.type = type
        self.menu = menu

    @staticmethod
    def get_meal_by_date(date: datetime) -> List['MealModel']:
        return MealModel.query.filter_by(date=date).order_by('type')

    @staticmethod
    def save_meal(date: datetime, type: int, menu: str):
        meals: List['MealModel'] = MealModel.query.filter_by(date=date).all()

        for meal in meals:
            meal.delete()

        MealModel(date, type, menu).save()

    @db.validates('type')
    def validate_type(self, key, type):
        self.assert_validation(type in [0, 1, 2])
        return type
