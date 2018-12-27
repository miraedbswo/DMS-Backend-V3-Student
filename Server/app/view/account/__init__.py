from flask import Blueprint
from flask_restful import Api


account_blueprint = Blueprint('account', __name__, url_prefix='/account')
api = Api(account_blueprint)


from .auth import AuthView
api.add_resource(AuthView, '/auth')

from .info import ExtensionInfoView, BasicInfoView, PointInfoView
api.add_resource(ExtensionInfoView, '/info/extension')
api.add_resource(BasicInfoView, '/info/basic')
api.add_resource(PointInfoView, '/info/point')

from .manage import ChangePasswordView, FindPasswordView
api.add_resource(ChangePasswordView, '/change-pw')
api.add_resource(FindPasswordView, '/find-pw')

from .signup import SignupView
api.add_resource(SignupView, '/signup')
