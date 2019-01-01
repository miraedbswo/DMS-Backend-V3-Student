from app.extension import db


class MealModel(db.Model):
    __tablename__ = 'meal_model'
    date = db.Column(db.Date, primary_key=True)
    type = db.Column(db.Enum('breakfast', 'lunch', 'dinner'))
    meal = db.Column(db.String)     # ,로 구분하여 입력
