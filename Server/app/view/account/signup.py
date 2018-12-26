from app.view.base_resource import AccountResource


class SignupView(AccountResource):

    def post(self):
        return '', 201
