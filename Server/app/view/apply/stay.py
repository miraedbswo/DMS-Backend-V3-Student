from flasgger import swag_from
from flask_jwt_extended import jwt_required

from app.doc.apply.stay import STAY_GET, STAY_POST
from app.view.base_resource import ApplyResource


class StayView(ApplyResource):
    @swag_from(STAY_GET)
    @jwt_required
    def get(self):
        pass

    @swag_from(STAY_POST)
    @jwt_required
    def post(self):
        pass
