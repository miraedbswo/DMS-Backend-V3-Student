from flask import Response

from test import TCBase, check_status_code
from test.request import ApplyRequest
from app.model.apply import MusicApplyModel


class TestGetMusic(TCBase, ApplyRequest):
    @check_status_code(200)
    def test_get_music_apply_status(self) -> Response:
        test_music_apply_data = {
            'singer': '아이유',
            'song_name': '삐삐',
            'studentId': 'test'
        }
        MusicApplyModel.post_music_apply(
            day=0,
            student_id=self.test_student_id,
            singer=test_music_apply_data['singer'],
            song_name=test_music_apply_data['song_name']
        )

        rv: Response = self.request_music_get()
        self.assertIsNotNone(rv.json)

        rv_data = {
            'singer': rv.json['mon'][0]['singer'],
            'song_name': rv.json['mon'][0]['musicName'],
            'studentId': rv.json['mon'][0]['studentId']
        }

        self.assertDictEqual(test_music_apply_data, rv_data)
        return rv

    @check_status_code(204)
    def test_no_content_music(self) -> Response:
        rv: Response = self.request_music_get()

        return rv

