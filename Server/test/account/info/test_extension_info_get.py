from datetime import datetime

from flask import Response

from app.model import ExtensionApplyModel, GoingOutApplyModel, StayApplyModel
from test import TCBase, check_status_code
from test.request import InfoRequest


class TestGetApplyInfo(TCBase, InfoRequest):
    @check_status_code(200)
    def test_success_get_extension11_info(self) -> Response:
        apply = {
            'classNum': 2,
            'seatNum': 12
        }

        ExtensionApplyModel.post_extension_apply('test', 11, 2, 12)
        rv: Response = self.request_apply_info(self.access_token)

        self.assertDictEqual(apply, rv.json['extension11'])
        return rv

    @check_status_code(200)
    def test_success_get_extension12_info(self):
        apply = {
            'classNum': 2,
            'seatNum': 12
        }

        ExtensionApplyModel.post_extension_apply('test', 12, 2, 12)
        rv = self.request_apply_info(self.access_token)

        self.assertDictEqual(apply, rv.json['extension12'])
        return rv

    @check_status_code(200)
    def test_success_get_going_out_info(self):
        apply = [
            {
                'goOutDate': '2019-01-01 12:30:00',
                'returnDate': '2019-01-01 17:30:00',
                'reason': '영화 관람'
            }
        ]

        GoingOutApplyModel.post_goingout_apply(
            'test',
            datetime(2019, 1, 1, 12, 30),
            datetime(2019, 1, 1, 17, 30),
            '영화 관람'
        )
        rv = self.request_apply_info(self.access_token)

        self.assertListEqual(apply, rv.json['goingOut'])
        return rv

    @check_status_code(200)
    def test_success_get_stay_info(self):
        apply = 1

        StayApplyModel.post_stay_apply('test', 1)
        rv: Response = self.request_apply_info(self.access_token)
        self.assertEqual(apply, rv.json['stay'])
        return rv

    @check_status_code(403)
    def test_validate_wrong_token(self):
        rv: Response = self.request_apply_info('fake_jwt_token')

        return rv
