from unittest import TestCase

from app import create_app


class TCBase(TestCase):
    def __init__(self):
        self.app = create_app()

        self.test_client = self.app.test_client()
        super(TCBase, self).__init__()