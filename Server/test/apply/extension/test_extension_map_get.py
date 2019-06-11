from flask import Response

from app.model.apply import ExtensionApplyModel
from test import TCBase, check_status_code
from test.request import ApplyRequest


class TestGetExtensionMap(TCBase, ApplyRequest):
    pass