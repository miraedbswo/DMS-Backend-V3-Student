from app.doc.apply.music import MUSIC_GET, MUSIC_POST
from app.view.base_resource import ApplyResource

from flasgger import swag_from


class MusicView(ApplyResource):
    @swag_from(MUSIC_GET)
    def get(self):
        pass

    @swag_from(MUSIC_POST)
    def post(self):
        pass
