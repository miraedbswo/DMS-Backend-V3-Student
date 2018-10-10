from flask import Blueprint
from flask_restful import Api


apply_blueprint = Blueprint('apply', __name__, url_prefix='/apply')
api = Api(apply_blueprint)


from .extension import ExtensionView
api.add_resource(ExtensionView, '/extension/<int:time>')

from .goingout import GoingoutView
api.add_resource(GoingoutView, '/goingout/<day>')

from .stay import StayView
api.add_resource(StayView, '/stay')