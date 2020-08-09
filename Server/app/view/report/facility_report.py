from flasgger import swag_from
from flask import request, Response
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.context import context_property
from app.doc.report.facility_report import FACILITY_REPORT_POST
from app.model import FacilityReportModel
from app.util.validate import data_type_validate, FACILITY_POST_JSON
from app.view.base import ReportResource


class FacilityReport(ReportResource):
    @data_type_validate(FACILITY_POST_JSON)
    @swag_from(FACILITY_REPORT_POST)
    @jwt_required
    def post(self):
        payload = context_property.request_payload
        student_id = get_jwt_identity()

        room = payload.get('room')
        content = payload.get('content')

        FacilityReportModel.post_facility_report(student_id, room, content)
        return Response('', 201)
