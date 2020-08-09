from flask import Blueprint
from flask_restful import Api

apply_blueprint = Blueprint('apply', __name__, url_prefix='/apply')
api = Api(apply_blueprint)

from .extension import Extension, ExtensionMap

api.add_resource(Extension, '/extension/<int:time>')
api.add_resource(ExtensionMap, '/extension/map/<int:time>/<int:class_num>')

from .goingout import GoingOut, GoingOutDetail

api.add_resource(GoingOut, '/goingout')
api.add_resource(GoingOutDetail, '/goingout/<apply_id>')

from .music import Music

api.add_resource(Music, '/music')

from .stay import Stay

api.add_resource(Stay, '/stay')
