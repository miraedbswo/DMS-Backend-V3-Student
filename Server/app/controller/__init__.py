from Server.app.controller.account import account_blueprint


class Router:
    def __init__(self, app):
        self.app = app

    def register_blueprint(self):
        self.app.register_blueprint(account_blueprint)