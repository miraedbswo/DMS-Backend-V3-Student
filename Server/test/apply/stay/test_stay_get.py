from flask import Response

from test import TCBase, check_status_code
from test.request import ApplyRequest
from app.model.apply import StayApplyModel


class TestGetStay(TCBase, ApplyRequest):
    @check_status_code(200)
    def test_get_default_stay_apply_status(self) -> Response:
        rv: Response = self.request_stay_get(self.access_token)

        self.assertEqual(4, rv.json['value'])
        return rv

    @check_status_code(200)
    def test_get_set_stay_apply_status(self) -> Response:
        StayApplyModel.post_stay_apply('test', 1)
        rv: Response = self.request_stay_get(self.access_token)

        self.assertEqual(1, rv.json['value'])
        return rv
