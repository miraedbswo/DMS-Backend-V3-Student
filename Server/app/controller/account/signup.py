from app.controller.base_resource import AccountResource


class Signup(AccountResource):

    def post(self):
        return '', 201
