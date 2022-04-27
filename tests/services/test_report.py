from datetime import datetime

import pytest
from sqlalchemy import select

from app.models.base import session
from app.models.category import CategoryModel
from app.models.report import ReportModel
from app.models.request_history import RequestHistoryModel

from app.services.partner_bank import mock_success_response
from app.services.report import ReportService


class TestReportService:

    @pytest.fixture()
    def fixture_category(self):
        model = CategoryModel(
            id="3f1dbe6b-fddd-40e6-bfc4-aaf6e6cda430", name="Suspeitosa"
        )
        session.add(model)
        session.commit()

        return model

    @pytest.fixture()
    def fixture_request_history(self, fixture_customer):
        model = RequestHistoryModel(
            customer_id=fixture_customer.id,
            initial_date=datetime.now(),
            end_date=datetime.now(),
            status='success',
        )
        session.add(model)
        session.commit()

        return model

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
