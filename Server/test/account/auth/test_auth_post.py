from flask import Response
from flask_jwt_extended import get_jwt_identity

from test import TCBase, check_status_code
from test.request import AccountRequest


class TestSignedAccountAuth(TCBase, AccountRequest):
    def test_auth_response_type(self, data: dict):
        self.assertIsInstance(data, dict)

        self.assertIn('accessToken', data)
        self.assertIn('refreshToken', data)

        access_token = data['accessToken']
        refresh_token = data['refreshToken']

        self.assertIsInstance(access_token, str)
        self.assertIsInstance(refresh_token, str)

    def test_validate_token(self, data: dict):
        # 토큰 검증 방식
        pass

    @check_status_code(401)
    def test_wrong_id_type(self):
        # id 타입 변경 후 assert test
        rv = self.request_auth(id=1)
        return rv

    @check_status_code(401)
    def test_wrong_pw_type(self):
        # pw 타입 변경 후 assert test
        rv = self.request_auth(password=1)
        return rv

    @check_status_code(200)
    def test_login_success(self):
        # 맞는 id & pw 200 success
        rv = self.request_auth()
        rv_data = rv.data

        self.test_auth_response_type(rv_data)
        self.test_validate_token(rv_data)

        return rv


class TestUnsignedAccountAuth(TCBase):
    def test_email_send(self):
        # mocking 해서 email 보내고 uuid 검증
        pass
