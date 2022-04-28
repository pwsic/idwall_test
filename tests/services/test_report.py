import pytest
from sqlalchemy import select

from app.common.exceptions import ReportNotFoundException
from app.models.base import session
from app.models.report import ReportModel
from app.services.partner_bank import mock_success_response
from app.services.report import ReportService


class TestReportService:
    def test_report_should_create_record(
        self, app, fixture_request_history, fixture_category
    ):
        query = select(ReportModel).where(
            ReportModel.request_history_id == fixture_request_history.id
        )

        before_create = session.execute(query)
        before_create = before_create.scalar_one_or_none()
        assert before_create is None

        purchase_history_service = ReportService(session)
        transactions = mock_success_response(fixture_request_history.customer_id)
        purchase_history_service.create(transactions, fixture_request_history.id)

        after_create = session.execute(query)
        after_create = after_create.scalar_one_or_none()
        assert after_create is not None

    def test_get_report_should_return_result(self, app, fixture_report):
        service = ReportService(session)
        report = service.get_by_id(fixture_report.id)

        assert report is not None

    def test_get_report_should_return_raise_exception_due_not_found_resource(self, app):
        service = ReportService(session)

        with pytest.raises(ReportNotFoundException):
            service.get_by_id("aslkdfalsjdf")
