from app.model import ExtensionApplyModel, GoingoutApplyModel, StayApplyModel

from test import TCBase
from test.request import InfoRequest


class TestExtensionInfo(TCBase, InfoRequest):
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
        rv = self.request_extension_info(self.jwt)

        default_data = {
            "extension11": None,
            "extension12": None,
            "goingOut": [],
            "stay": 4
        }
        self.assertEqual(rv.data, default_data)

    # extension11, 12, goingOut, stay 설정 후 assertEqual
    def test_set_extension11_status(self):
        extension11_test_data = {
            'classNum': 2,
            'seatNum': 12
        }

        ExtensionApplyModel.post_extension_apply('test', 11, 2, 12)
        rv = self.request_extension_info(self.jwt)

        self.assertDictEqual(extension11_test_data, rv.data['extension11'])

    def test_set_extension12_status(self):
        extension12_test_data = {
            'classNum': 2,
            'seatNum': 12
        }

        ExtensionApplyModel.post_extension_apply('test', 12, 2, 12)
        rv = self.request_extension_info(self.jwt)

        self.assertDictEqual(extension12_test_data, rv.data['extension12'])

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
        rv = self.request_extension_info(self.jwt)

        self.assertListEqual(goingout_test_data, rv.data['goingOut'])

    def test_set_stay_status(self):
        stay_test_data = 1

        StayApplyModel.post_stay_apply('test', 1)
        rv = self.request_extension_info(self.jwt)

        self.assertEqual(stay_test_data, rv.data['stay'])
    @check_status_code(403)

