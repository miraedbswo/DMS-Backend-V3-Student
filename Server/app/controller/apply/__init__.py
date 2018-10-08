from flask import Blueprint
from flask_restful import Api


apply_blueprint = Blueprint('apply', __name__, url_prefix='/apply')
api = Api(apply_blueprint)


from .extension import Extension
api.add_resource(Extension, '/extension/<int:time>')

from .goingout import Goingout
api.add_resource(Goingout, '/goingout/<day>')

from .stay import Stay
api.add_resource(Stay, '/stay')