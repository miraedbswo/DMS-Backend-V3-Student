from flask import Response

from app.model.apply import ExtensionApplyModel
from test import TCBase, check_status_code
from test.request import ApplyRequest


class TestGetExtension(TCBase, ApplyRequest):
    @check_status_code(204)
    def test_get_default_extension_status(self) -> Response:
        rv: Response = self.request_extension_get(self.access_token, 11)

        return rv

    @check_status_code(200)
    def test_success_get_extension(self) -> Response:
        apply = {
            'classNum': 1,
            'seatNum': 16
        }

        ExtensionApplyModel.post_extension_apply(
            student_id='test',
            time=11,
            class_=apply.get('classNum'),
            seat=apply.get('seatNum'),
        )

        rv: Response = self.request_extension_get(self.access_token, 11)
        self.assertDictEqual(apply, rv.json)

        return rv
