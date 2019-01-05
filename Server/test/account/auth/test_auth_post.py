from flask import Response
from unittest import mock

from app.doc.account import SAMPLE_ACCESS_TOKEN, SAMPLE_REFRESH_TOKEN
from test import TCBase, check_status_code
from test.request import AccountRequest


class TestSignedAccountAuth(TCBase, AccountRequest):
    @check_status_code(200)
    def test_login_success(self):
        # 맞는 id & pw 200 success
        rv = self.request_auth()
        return rv

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
    @mock.patch('test.request.AccountRequest')
    def test_token(self, mock_get):
        # mock 해서 return 값 토큰을 sample_access_token & sample_refresh_token 발급
        # response 온 sample 값이 맞는지 assertEqual
        mock_resp = self._mock_response(content={
                "accessToken": SAMPLE_ACCESS_TOKEN,
                "refreshToken": SAMPLE_REFRESH_TOKEN
        })
        mock_get.return_value = mock_resp

        rv = self.request_auth()

        self.assertIsNotNone(rv)

        self.assertEqual(rv.json["accessToken"], SAMPLE_ACCESS_TOKEN)
        self.assertEqual(rv.json["refreshToken"], SAMPLE_REFRESH_TOKEN)


class TestUnsignedAccountAuth(TCBase):
    def __init__(self):
        super(TestUnsignedAccountAuth, self).__init__()

    def setUp(self):
        super(TestUnsignedAccountAuth, self).setUp()

    def test_email_send(self):
        # mocking 해서 email 보내고 uuid 검증
        pass
