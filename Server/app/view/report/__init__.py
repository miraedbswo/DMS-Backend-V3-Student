from flask import Blueprint
from flask_restful import Api

report_blueprint = Blueprint('report', __name__, url_prefix='/report')
api = Api(report_blueprint)

from .bug_report import BugReport

api.add_resource(BugReport, '/bug/<platform>')

from .facility_report import FacilityReport

api.add_resource(FacilityReport, '/facility')
