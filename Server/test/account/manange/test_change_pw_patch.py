import bcrypt
from flask import Response

from test import TCBase, check_status_code
from test.request import AccountRequest


class TestChangePassword(TCBase, AccountRequest):
    @check_status_code(205)
    def test_same_type_of_two_password(self) -> Response:
        # 현재 비밀번호와 새 비밀번호가 동일 할 때의 205 status code check
        rv: Response = self.request_change_pw(self.access_token, new_password='test')

        return rv

    @check_status_code(403)
    def test_wrong_current_password(self) -> Response:
        # 현재 비밀번호와 current pw 가 다를 때의 403 status code check
        rv: Response = self.request_change_pw(self.access_token, 'wrong_pw', 'new_pw')

        return rv

    @check_status_code(201)
    def test_password_change_successful(self) -> Response:
        rv: Response = self.request_change_pw(self.access_token)
        return rv
