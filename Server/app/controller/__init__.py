class Router:
    def __init__(self, app):
        self.app = app

    def register_blueprint(self):
        from .account import account_blueprint
        self.app.register_blueprint(account_blueprint)

        from .apply import apply_blueprint
        self.app.register_blueprint(apply_blueprint)
