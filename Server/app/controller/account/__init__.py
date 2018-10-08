from flask import Blueprint
from flask_restful import Api

account_blueprint = Blueprint('account', __name__)
api = Api(account_blueprint)


from .signup import Signup
api.add_resource(Signup, '/signup')
