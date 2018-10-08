from flask import Blueprint
from flask_restful import Api


account_blueprint = Blueprint('account', __name__, url_prefix='/account')
api = Api(account_blueprint)


from .auth import Auth
api.add_resource(Auth, '/auth')

from .info import Info
api.add_resource(Info, '/info/<type>')

from .manage import ChangePassword
api.add_resource(ChangePassword, '/password')

from .signup import Signup
api.add_resource(Signup, '/signup')
