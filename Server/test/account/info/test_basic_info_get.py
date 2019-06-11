from flask import Response

from app.model.point.status import PointStatusModel, message
from test import TCBase, check_status_code
from test.request import InfoRequest


class TestGetBasicInfo(TCBase, InfoRequest):
    def setUp(self):
        super(TestGetBasicInfo, self).setUp()

    @check_status_code(200)
    def test_success_get_default_basic_status(self) -> Response:
        status = {
            'badPoint': 0,
            'goodPoint': 0,
            'penaltyLevel': 0,
            'penaltyStatus': False
        }

        rv: Response = self.request_basic_info(self.access_token)
        PointStatusModel.get_point_status(student_id='test')

        self.assertEqual(rv.json.get('badPoint'), status.get('badPoint'))
        self.assertEqual(rv.json.get('goodPoint'), status.get('goodPoint'))
        self.assertEqual(rv.json.get('penaltyLevel'), status.get('penaltyLevel'))
        self.assertEqual(rv.json.get('penaltyStatus'), status.get('penaltyStatus'))

        return rv
