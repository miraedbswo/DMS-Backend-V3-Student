from flask import Response

from test import TCBase, check_status_code
from test.request import InfoRequest


class TestPointInfo(TCBase, InfoRequest):
    @check_status_code(200)
    def test_default_point_status(self) -> Response:
        default_data = []
        rv: Response = self.request_point_info(self.access_token)

        self.assertEqual(default_data, rv.json['point_history'])

        return rv

    @check_status_code(200)
    def test_set_point_status(self) -> Response:
        # point setup 기능은 Admin 권한만 가능함.
        pass

    @check_status_code(403)
    def test_point_info_forbidden(self) -> Response:
        rv: Response = self.request_point_info('fake_jwt_token')

        return rv
