from app.doc.report.bug_report import BUG_REPORT_POST
from app.view.base_resource import ReportResource

from flasgger import swag_from


class BugReportView(ReportResource):
    @swag_from(BUG_REPORT_POST)
    def post(self, platform):
        pass
