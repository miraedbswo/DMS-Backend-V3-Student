from flask import Response
from freezegun import freeze_time

from test import TCBase, check_status_code
from test.request import ApplyRequest
from app.model.apply import MusicApplyModel


class TestPostMusic(TCBase, ApplyRequest):
    @check_status_code(201)
    def test_post_music_apply_status(self) -> Response:
        test_music_apply_data = {
            'singer': '아이유',
            'song_name': '삐삐'
        }
        rv: Response = self.request_music_post(
            self.access_token,
            test_music_apply_data['singer'],
            test_music_apply_data['song_name']
        )

        status = MusicApplyModel.get_music_apply_status()
        status_data = {
            'singer': status['mon'].singer,
            'song_name': status['mon'].musicName
        }

        self.assertDictEqual(test_music_apply_data, status_data)

        return rv

    @check_status_code(205)
    def test_apply_music_data_completed(self):
        for _ in range(5):
            MusicApplyModel.post_music_apply(0, 'test', 'singer', 'song')

        rv: Response = self.request_music_post(self.access_token, 'test', 'test')
        return rv
    
    @freeze_time('2019-01-04 18:00:00')
    @check_status_code(409)
    def test_apply_music_outside_time(self) -> Response:
        rv: Response = self.request_music_post(
            self.access_token,
            '아이유',
            '삐삐'
        )

        return rv
