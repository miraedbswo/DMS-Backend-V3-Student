from flask import Blueprint
from flask_restful import Api


report_blueprint = Blueprint('report', __name__, url_prefix='/report')
api = Api(report_blueprint)


from .bug_report import BugReportView
api.add_resource(BugReportView, '/bug/<platform>')

from .facility_report import FacilityReportView
api.add_resource(FacilityReportView, '/facility')
