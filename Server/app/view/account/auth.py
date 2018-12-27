from app.doc.account.auth import AUTH_POST
from app.view.base_resource import AccountResource

from flasgger import swag_from


class AuthView(AccountResource):
    @swag_from(AUTH_POST)
    def post(self):
        pass
