from flask import Blueprint
from flask_restful import Api


account_blueprint = Blueprint('account', __name__, url_prefix='/account')
account_api = Api(account_blueprint)

info_blueprint = Blueprint('info', __name__, url_prefix='/info')
info_api = Api(info_blueprint)


from .auth import AuthView
account_api.add_resource(AuthView, '/auth')

from .info import ExtensionInfoView, BasicInfoView, PointInfoView
info_api.add_resource(ExtensionInfoView, '/extension')
info_api.add_resource(BasicInfoView, '/basic')
info_api.add_resource(PointInfoView, '/point')

from .manage import ManagePasswordView
account_api.add_resource(ManagePasswordView, '/pw')

from .signup import SignupView
account_api.add_resource(SignupView, '/signup')
