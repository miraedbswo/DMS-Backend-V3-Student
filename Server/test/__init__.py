from functools import wraps
from flask_jwt_extended import create_access_token

import unittest
from unittest.mock import Mock
from app import create_app
from app.extension import db


class TCBase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.app = create_app('testing')
        self.client = self.app.test_client()

        """
        flask_jwt_extended.create_access_token() 함수 내부에서, 
        current_app.extensions['flask-jwt-extended'] 을 호출함.
        current_app 객체는 application context 내부에서만 사용할 수 있으므로
        test_context를 만들어 주고 json web token을 context 내부에서 생성한다.
        """
        self.test_context = self.app.app_context()

        with self.test_context:
            self.jwt = create_access_token('test')

        super(TCBase, self).__init__(*args, **kwargs)

    def setUp(self):
        self.db = db
        db.create_all(app=self.app)

    def tearDown(self):
        db.session.remove()
        db.drop_all(app=self.app)

    def _mock_response(
            self,
            content: dict,
            status: int = 200) -> Mock:
        mock_resp = Mock()

        mock_resp.status_code = status
        mock_resp.content = content
        return mock_resp


def check_status_code(status_code):
    def decorator(fn):
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            rv = fn(self, *args, **kwargs)
            self.assertEqual(rv.status_code, status_code)

        return wrapper

    return decorator
