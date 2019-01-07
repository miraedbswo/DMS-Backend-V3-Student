from functools import wraps

import unittest
from unittest.mock import Mock
from app import create_app
from app.extension import db


class TCBase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.jwt = create_access_token('test',
    def setUp(self):
        self.db = db

        self.app = create_app('testing')
        self.client = self.app.test_client()
        db.create_all(app=self.app)

    def tearDown(self):
        db.session.remove()
        db.drop_all(app=self.app)

    def _mock_response(
            self,
            content: dict,
            status: int = 200):

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
