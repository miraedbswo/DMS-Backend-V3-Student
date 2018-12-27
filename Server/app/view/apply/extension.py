from app.doc.apply.extension import EXTENSION_GET, EXTENSION_POST, EXTENSION_DELETE, EXTENSION_MAP_GET
from app.view.base_resource import ApplyResource

from flasgger import swag_from


class ExtensionView(ApplyResource):
    @swag_from(EXTENSION_GET)
    def get(self, time):
        # 11 or 12
        pass

    @swag_from(EXTENSION_POST)
    def post(self, time):
        pass

    @swag_from(EXTENSION_DELETE)
    def delete(self, time):
        pass


class ExtensionMapView(ApplyResource):
    @swag_from(EXTENSION_MAP_GET)
    def get(self, time):
        pass
