from datetime import date, timedelta

from flask import Response

from app.model.apply import MusicApplyModel
from test import TCBase, check_status_code
from test.request import ApplyRequest

tomorrow = str(date.today() + timedelta(1))


class TestPostMusic(TCBase, ApplyRequest):
    @check_status_code(201)
    def test_success(self) -> Response:
        test_music_apply_data = {
            'singer': '아이유',
            'song_name': '삐삐',
            'studentId': 'test'
        }
        rv: Response = self.request_music_post(
            self.access_token,
            0,
            test_music_apply_data['singer'],
            test_music_apply_data['song_name']
        )

        status = MusicApplyModel.get_music_apply_status()
        status_data = {
            'singer': status['mon'][0]['singer'],
            'song_name': status['mon'][0]['musicName'],
            'studentId': status['mon'][0]['studentId']
        }

        self.assertDictEqual(test_music_apply_data, status_data)

        return rv

    @check_status_code(205)
    def test_apply_music_completed(self):
        for _ in range(5):
            MusicApplyModel.post_music_apply(0, 'test', 'singer', 'song')

        rv: Response = self.request_music_post(self.access_token, 0, 'test', 'test')
        return rv
