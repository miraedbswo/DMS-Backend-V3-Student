from flask import Blueprint
from flask_restful import Api

apply_blueprint = Blueprint('apply', __name__, url_prefix='/apply')
api = Api(apply_blueprint)

from .extension import ExtensionView, ExtensionMapView

api.add_resource(ExtensionView, '/extension/<int:time>')
api.add_resource(ExtensionMapView, '/extension/map/<int:time>/<int:class_num>')

from .goingout import GoingOutView

api.add_resource(GoingOutView, '/goingout')

from .music import MusicView

api.add_resource(MusicView, '/music')

from .stay import StayView

api.add_resource(StayView, '/stay')
