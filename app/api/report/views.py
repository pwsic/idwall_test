from flask_restx import Namespace, Resource, abort

from app.api.history.schema import history_post_schema
from app.common.exceptions import ReportNotFoundException
from app.models.base import session
from app.services.report import ReportService

report_api = Namespace("report", "Report  API")

resource_fields = report_api.model("Resource", history_post_schema)


@report_api.route("/<report_id>")
class Report(Resource):
    @report_api.doc(params={"report_id": "Report ID"})
    def get(self, report_id):
        response = {}
        try:
            service = ReportService(session)
            report = service.get_by_id(report_id)

            response.update({"id": report.customer_id, "expenses": report.expenses})

        except ReportNotFoundException:
            abort(404, "Report not found")
        return response
