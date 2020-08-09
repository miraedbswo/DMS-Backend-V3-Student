from flasgger import swag_from
from flask import request, Response
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.context import context_property
from app.doc.apply.music import MUSIC_GET, MUSIC_POST, MUSIC_DELETE
from app.exception import ApplyTimeException
from app.model import MusicApplyModel
from app.util.validate import data_type_validate, MUSIC_POST_JSON, MUSIC_DELETE_JSON
from app.view.base import ApplyResource


class Music(ApplyResource):
    @swag_from(MUSIC_GET)
    @jwt_required
    def get(self):
        return MusicApplyModel.get_music_apply_status()

    @data_type_validate(MUSIC_POST_JSON)
    @swag_from(MUSIC_POST)
    @jwt_required
    def post(self):
        payload = context_property.request_payload
        apply_time = self.kst_now()

        if (apply_time.weekday() == 5) or \
                (apply_time.weekday() == 6 and apply_time.hour <= 9 and apply_time.minute <= 30):
            raise ApplyTimeException

        student_id = get_jwt_identity()
        day = payload.get('day')
        singer = payload.get('singer')
        song_name = payload.get('musicName')

        MusicApplyModel.post_music_apply(day, student_id, singer, song_name)
        return Response('', 201)

    @data_type_validate(MUSIC_DELETE_JSON)
    @swag_from(MUSIC_DELETE)
    @jwt_required
    def delete(self):
        payload = context_property.request_payload
        student_id = get_jwt_identity()

        apply_id = payload.get('apply_id')

        MusicApplyModel.delete_music_apply(student_id, apply_id)
        return Response('', 200)
