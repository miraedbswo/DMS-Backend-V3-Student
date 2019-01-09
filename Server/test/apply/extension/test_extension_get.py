from flask import Response
from freezegun import freeze_time

from test import TCBase, check_status_code
from test.request import ApplyRequest
from app.model.apply import ExtensionApplyModel


class TestGetExtension(TCBase, ApplyRequest):
    @check_status_code(204)
    def test_extension_default_status(self) -> Response:
        rv: Response = self.request_extension_get(self.access_token, 11)

        return rv

    @check_status_code(200)
    def test_get_extension_successful(self) -> Response:
        extension_data = {
            'classNum': 1,
            'seatNum': 16
        }

        ExtensionApplyModel.post_extension_apply(
            student_id='test',
            time=11,
            class_=extension_data['classNum'],
            seat=extension_data['seatNum']
        )

        rv: Response = self.request_extension_get(self.access_token, 11)
        self.assertDictEqual(extension_data, rv.json)

        return rv
