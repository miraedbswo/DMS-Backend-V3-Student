class Router:
    def __init__(self, app):
        self.app = app

    def register_blueprint(self):
        from .account import account_blueprint
        self.app.register_blueprint(account_blueprint)

        from .apply import apply_blueprint
        self.app.register_blueprint(apply_blueprint)

        from .meal import meal_blueprint
        self.app.register_blueprint(meal_blueprint)

        from .notice import notice_blueprint
        self.app.register_blueprint(notice_blueprint)

        from .report import report_blueprint
        self.app.register_blueprint(report_blueprint)

        from .survey import survey_blueprint
        self.app.register_blueprint(survey_blueprint)
