from test import TCBase, check_status_code
from test.request import InfoRequest


class TestPointInfo(TCBase, InfoRequest):
    @check_status_code(200)
    def test_default_point_status(self):
        default_data = []
        rv = self.request_point_info(self.jwt)

        self.assertEqual(default_data, rv.json)

        return rv

    @check_status_code(200)
    def test_set_point_status(self):
        # point setup 기능은 Admin 권한만 가능함.
        pass

    @check_status_code(403)
    def test_point_info_forbidden(self):
        rv = self.request_point_info('fake_jwt_token')

        return rv
