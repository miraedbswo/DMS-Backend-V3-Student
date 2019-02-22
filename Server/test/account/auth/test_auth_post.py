from flask import Response

from test import TCBase, check_status_code
from test.request import AccountRequest


class TestSignedAccountAuth(TCBase, AccountRequest):
    def auth_response_type(self, data: dict):
        self.assertIsInstance(data, dict)

        self.assertIn('accessToken', data)
        self.assertIn('refreshToken', data)

        access_token = data['accessToken']
        refresh_token = data['refreshToken']

        self.assertIsInstance(access_token, str)
        self.assertIsInstance(refresh_token, str)

    def validate_token(self, data: dict):
        # 토큰 검증 방식
        pass

    @check_status_code(400)
    def test_wrong_id_type(self) -> Response:
        # id 타입 변경 후 assert test
        rv: Response = self.request_auth(id=1)

        return rv

    @check_status_code(400)
    def test_wrong_pw_type(self) -> Response:
        # pw 타입 변경 후 assert test
        rv: Response = self.request_auth(password=1)
        return rv

    @check_status_code(200)
    def test_login_success(self) -> Response:
        # 맞는 id & pw 200 success
        rv: Response = self.request_auth()
        rv_data = rv.json

        self.auth_response_type(rv_data)
        self.validate_token(rv_data)

        return rv


class TestUnsignedAccountAuth(TCBase):
    def test_email_send(self) -> Response:
        # mocking 해서 email 보내고 uuid 검증
        pass
