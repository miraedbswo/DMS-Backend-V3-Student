from app.model import ExtensionApplyModel, GoingoutApplyModel, StayApplyModel

from test import TCBase, check_status_code
from test.request import InfoRequest


class TestApplyInfo(TCBase, InfoRequest):
    @check_status_code(200)
    def test_extension_default_status(self):
        """
        default status 검증
        {
            'extension11': None
            'extension12': None,
            'goingOut': [None],
            'stay': 4
        }
        """
        default_data = {
            "extension11": None,
            "extension12": None,
            "goingOut": [],
            "stay": 4
        }

        rv = self.request_apply_info(self.access_token)

        self.assertDictEqual(default_data, rv.json)
        return rv

    # extension11, 12, goingOut, stay 설정 후 assertEqual
    @check_status_code(200)
    def test_set_extension11_status(self):
        extension11_test_data = {
            'classNum': 2,
            'seatNum': 12
        }

        ExtensionApplyModel.post_extension_apply('test', 11, 2, 12)
        rv = self.request_apply_info(self.access_token)

        self.assertDictEqual(extension11_test_data, rv.json['extension11'])
        return rv

    @check_status_code(200)
    def test_set_extension12_status(self):
        extension12_test_data = {
            'classNum': 2,
            'seatNum': 12
        }

        ExtensionApplyModel.post_extension_apply('test', 12, 2, 12)
        rv = self.request_apply_info(self.access_token)

        self.assertDictEqual(extension12_test_data, rv.json['extension12'])
        return rv

    @check_status_code(200)
    def test_set_goingout_status(self):
        goingout_test_data = [
            {
                'goOutDate': '2019-01-01 12:30',
                'reason': '2019-01-01 17:30',
                'returnDate': '영화 관람'
            }
        ]

        GoingoutApplyModel.post_goingout_apply(
            'test',
            '2019-01-01 12:30',
            '2019-01-01 17:30',
            '영화 관람'
        )
        rv = self.request_apply_info(self.access_token)

        self.assertListEqual(goingout_test_data, rv.json['goingOut'])
        return rv

    @check_status_code(200)
    def test_set_stay_status(self):
        stay_test_data = 1

        StayApplyModel.post_stay_apply('test', 1)
        rv = self.request_apply_info(self.access_token)
        self.assertEqual(stay_test_data, rv.json['stay'])
        return rv

    @check_status_code(403)
    def test_apply_info_forbidden(self):
        rv = self.request_apply_info('fake_jwt_token')

        return rv
