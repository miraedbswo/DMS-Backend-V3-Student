from flask import Blueprint
from flask_restful import Api


account_blueprint = Blueprint('account', __name__, url_prefix='/account')
api = Api(account_blueprint)


from .auth import AuthView
api.add_resource(AuthView, '/auth')

from .info import InfoView
api.add_resource(InfoView, '/info/<type>')

from .manage import ChangePasswordView
api.add_resource(ChangePasswordView, '/password')

from .signup import SignupView
api.add_resource(SignupView, '/signup')
