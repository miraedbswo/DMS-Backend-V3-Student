from app.doc.account.signup import SIGNUP_POST
from app.view.base_resource import AccountResource

from flasgger import swag_from


class SignupView(AccountResource):
    @swag_from(SIGNUP_POST)
    def post(self):
        pass
