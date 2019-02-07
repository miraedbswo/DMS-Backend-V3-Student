from flask import Response

from test import TCBase, check_status_code
from test.request import NoticeRequest
from app.model.notice import NoticeModel


class TestGetNotice(TCBase, NoticeRequest):
    # @check_status_code(201)
    # def test_post_stay_successful(self):
    #     rv: Response = self.request_stay_post(self.access_token, 1)
    #     status = StayApplyModel.get_stay_apply_status('test')
    #     self.assertEqual(1, status['value'])
    #     return rv
    #
    # @check_status_code(409)
    # def test_post_stay_outside_time(self):
    #     rv: Response = self.request_stay_post(self.access_token, 1)
    #     status = StayApplyModel.get_stay_apply_status('test')
    #     self.assertEqual(4, status['value'])
    #     return rv
    pass