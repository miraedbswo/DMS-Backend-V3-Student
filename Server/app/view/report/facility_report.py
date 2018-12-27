from app.doc.report.facility_report import FACILITY_REPORT_POST
from app.view.base_resource import ReportResource

from flasgger import swag_from


class FacilityReportView(ReportResource):
    @swag_from(FACILITY_REPORT_POST)
    def post(self):
        pass
