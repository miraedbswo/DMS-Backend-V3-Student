from functools import wraps

import unittest
from app import create_app
from app.extension import db


class TCBase(unittest.TestCase):
    def __init__(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        super(TCBase, self).__init__()

    def setUp(self):
        self.db = db
        db.create_all(app=self.app)

    def tearDown(self):
        db.session.remove()
        db.drop_all(app=self.app)


def check_status_code(status_code):
    def decorator(fn):
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            rv = fn(self, *args, **kwargs)
            self.assertEqual(rv.status_code, status_code)
        return wrapper
    return decorator
