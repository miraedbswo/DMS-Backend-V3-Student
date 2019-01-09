from flask import Response
from freezegun import freeze_time

from test import TCBase, check_status_code
from test.request import ApplyRequest
from app.model.apply import StayApplyModel


class TestPostStay(TCBase, ApplyRequest):
    @check_status_code(200)
    def test_post_stay_successful(self):
        rv: Response = self.request_stay_post(self.access_token, 1)

        status = StayApplyModel.get_stay_apply_status('test')
        self.assertEqual(1, status['value'])

        return rv

    @freeze_time('2019-01-04 00:00:00')
    @check_status_code(204)
    def test_post_stay_outside_time(self):
        rv: Response = self.request_stay_post(self.access_token, 1)

        status = StayApplyModel.get_stay_apply_status('test')
        self.assertEqual(4, status['value'])

        return rv
