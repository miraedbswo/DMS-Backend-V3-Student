from flask import Response

from test import TCBase, check_status_code
from test.request import InfoRequest


class TestBasicInfo(TCBase, InfoRequest):
    @check_status_code(200)
    def test_default_basic_status(self) -> Response:
        rv: Response = self.request_basic_info(self.access_token)
        # test 계정 default 값 지정

        return rv
