from app.doc.account.manage import CHANGE_PW_PATCH, FIND_PW_POST
from app.view.base_resource import AccountResource

from flasgger import swag_from


class ManagePasswordView(AccountResource):
    @swag_from(CHANGE_PW_PATCH)
    def patch(self):
        pass

    @swag_from(FIND_PW_POST)
    def post(self):
        pass
