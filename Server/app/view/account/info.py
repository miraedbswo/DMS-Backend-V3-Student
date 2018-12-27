from app.doc.account.info import EXTENSION_INFO_GET, BASIC_INFO_GET, POINT_HISTORY_GET
from app.view.base_resource import AccountResource

from flasgger import swag_from


class ExtensionInfoView(AccountResource):
    @swag_from(EXTENSION_INFO_GET)
    def get(self):
        pass


class BasicInfoView(AccountResource):
    @swag_from(BASIC_INFO_GET)
    def get(self):
        pass


class PointInfoView(AccountResource):
    @swag_from(POINT_HISTORY_GET)
    def get(self):
        pass
