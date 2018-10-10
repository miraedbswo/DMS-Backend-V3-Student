from app.controller.base_resource import AccountResource


class SignupView(AccountResource):

    def post(self):
        return '', 201
