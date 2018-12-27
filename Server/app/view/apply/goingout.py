from app.doc.apply.goingout import GOINGOUT_GET, GOINGOUT_POST
from app.view.base_resource import ApplyResource

from flasgger import swag_from


class GoingOutView(ApplyResource):
    @swag_from(GOINGOUT_GET)
    def get(self):
        pass

    @swag_from(GOINGOUT_POST)
    def post(self):
        pass
