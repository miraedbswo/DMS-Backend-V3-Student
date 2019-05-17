from flask import Blueprint
from flask_restful import Api

account_blueprint = Blueprint('account', __name__, url_prefix='/account')
account_api = Api(account_blueprint)

info_blueprint = Blueprint('info', __name__, url_prefix='/info')
info_api = Api(info_blueprint)

from .auth import Auth, Refresh

account_api.add_resource(Auth, '/auth')
account_api.add_resource(Refresh, '/refresh')

from .info import ApplyInfo, BasicInfo, PointInfo

info_api.add_resource(ApplyInfo, '/apply')
info_api.add_resource(BasicInfo, '/basic')
info_api.add_resource(PointInfo, '/point')

from .manage import ManagePassword, FindPWGet

account_api.add_resource(ManagePassword, '/pw')
account_api.add_resource(FindPWGet, '/pw/<uuid>')

from .signup import Signup

account_api.add_resource(Signup, '/signup')
