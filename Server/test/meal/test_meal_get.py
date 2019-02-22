from datetime import date

from flask import Response

from app.model.meal import MealModel
from test import TCBase, check_status_code
from test.request import MealRequest


class TestGetMeal(TCBase, MealRequest):
    @check_status_code(200)
    def test_get_no_content_meal(self) -> Response:
        rv: Response = self.request_meal('2019-01-01')

        for values in rv.json.values():
            self.assertIsNone(values)

        return rv

    @check_status_code(200)
    def test_get_setup_meal(self) -> Response:
        MealModel.save_meal(date(2019, 1, 1), 1, '아침||점심||저녁')
        rv: Response = self.request_meal('2019-01-01')

        for values in rv.json.values():
            self.assertEqual('아침' or '점심' or '저녁', values)

        return rv

    @check_status_code(205)
    def test_get_meal_wrong_date(self) -> Response:
        rv: Response = self.request_meal('2019-01-00')

        return rv
