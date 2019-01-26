from flasgger import swag_from
from flask_jwt_extended import jwt_required

from app.doc.report.facility_report import FACILITY_REPORT_POST
from app.view.base_resource import ReportResource


class FacilityReportView(ReportResource):
    @swag_from(FACILITY_REPORT_POST)
    @jwt_required
    def post(self):
        pass
