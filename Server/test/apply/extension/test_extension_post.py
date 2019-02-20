from datetime import date, timedelta
from flask import Response
from freezegun import freeze_time

from test import TCBase, check_status_code
from test.request import ApplyRequest
from app.model.apply import ExtensionApplyModel


tomorrow = str(date.today() + timedelta(1))


class TestPostExtension(TCBase, ApplyRequest):
    @freeze_time(f'{tomorrow} 20:00:00')
    @check_status_code(201)
    def test_apply_extension_success(self) -> Response:
        rv: Response = self.request_extension_post(self.access_token, 11, 1, 16)

        self.assertIsNotNone(ExtensionApplyModel.get_extension_apply_status('test', 11))
        return rv

    @freeze_time(f'{tomorrow} 10:30:00')
    @check_status_code(409)
    def test_11_apply_extension_outside_time(self) -> Response:
        rv: Response = self.request_extension_post(self.access_token, 11, 1, 16)

        self.assertIsNone(ExtensionApplyModel.get_extension_apply_status('test', 11))
        return rv

    @freeze_time(f'{tomorrow} 10:30:00')
    @check_status_code(409)
    def test_12_apply_extension_outside_time(self) -> Response:
        rv: Response = self.request_extension_post(self.access_token, 12, 1, 16)

        self.assertIsNone(ExtensionApplyModel.get_extension_apply_status('test', 12))
        return rv

    @freeze_time(f'{tomorrow} 20:00:00')
    @check_status_code(205)
    def test_apply_extension_already_applied_seat(self) -> Response:
        ExtensionApplyModel(
            student_id='test',
            time=11,
            class_=1,
            seat=16
        ).save()

        rv: Response = self.request_extension_post(self.access_token, 11, 1, 16)

        return rv
