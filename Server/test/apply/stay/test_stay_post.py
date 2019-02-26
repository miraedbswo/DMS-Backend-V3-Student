from datetime import date, timedelta

from flask import Response
from freezegun import freeze_time

from app.model.apply import StayApplyModel
from test import TCBase, check_status_code
from test.request import ApplyRequest

time = str(date.today() + timedelta(6 - date.today().weekday()))


class TestPostStay(TCBase, ApplyRequest):
    @check_status_code(201)
    def test_post_stay_successful(self):
        rv: Response = self.request_stay_post(self.access_token, 1)

        status = StayApplyModel.get_stay_apply_status('test')
        self.assertEqual(1, status['value'])

        return rv

    @freeze_time(f'{time} 00:00:00')
    @check_status_code(409)
    def test_post_stay_outside_time(self):
        rv: Response = self.request_stay_post(self.access_token, 1)

        status = StayApplyModel.get_stay_apply_status('test')
        self.assertEqual(4, status['value'])

        return rv
