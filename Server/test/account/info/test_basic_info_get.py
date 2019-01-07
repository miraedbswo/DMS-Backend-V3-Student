from test import TCBase, check_status_code
from test.request import InfoRequest


class TestBasicInfo(TCBase, InfoRequest):
    @check_status_code(200)
    def test_default_basic_status(self):
        rv = self.request_basic_info(self.jwt)
        # test 계정 default 값 지정

        return rv
