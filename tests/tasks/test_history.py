from datetime import datetime
from unittest.mock import patch

import pytest
from sqlalchemy import select

from app.common.exceptions import PartnerBankTimemoutException
from app.models.base import session
from app.models.request_history import RequestHistoryModel
from app.services.classifier import ClassifierService
from app.services.partner_bank import mock_success_response
from app.services.report import ReportService
from app.services.request_history import RequestHistoryService
from app.tasks.history import track_history


class TestTrackHistory:
    @pytest.fixture()
    def fixture_request_history(self, fixture_customer):
        model = RequestHistoryModel(
            customer_id=fixture_customer.id,
            initial_date=datetime.now(),
            end_date=datetime.now(),
            status="init",
        )
        session.add(model)
        session.commit()

        return model

    @patch.object(ReportService, "create")
    @patch.object(ClassifierService, "classify")
    def test_history_should_work(
        self, mock_classify, mock_report_service, app, fixture_request_history
    ):
        query = select(RequestHistoryModel).where(
            RequestHistoryModel.id == fixture_request_history.id
        )

        before_update = session.execute(query)
        before_update = before_update.scalar_one_or_none()
        assert before_update.status == "init"

        with patch.object(RequestHistoryService, "get_history_by_period") as mocky:
            mocky.return_value = mock_success_response(before_update.customer_id)
            result = track_history(fixture_request_history.id)

        assert result["id"] is not None

        after_update = session.execute(query)
        after_update = after_update.scalar_one_or_none()
        assert after_update.status == "success"

        assert mock_classify.called
        assert mock_report_service.called

    @patch.object(ReportService, "create")
    @patch.object(ClassifierService, "classify")
    def test_history_should_error(
        self, mock_classify, mock_report_service, app, fixture_request_history
    ):
        query = select(RequestHistoryModel).where(
            RequestHistoryModel.id == fixture_request_history.id
        )

        before_update = session.execute(query)
        before_update = before_update.scalar_one_or_none()
        assert before_update.status == "init"

        with patch.object(RequestHistoryService, "get_history_by_period") as mocky:
            mocky.side_effect = PartnerBankTimemoutException("Service Unavailable")
            result = track_history(fixture_request_history.id)

        assert result == {}

        after_update = session.execute(query)
        after_update = after_update.scalar_one_or_none()
        assert after_update.status == "error"

        assert not mock_classify.called
        assert not mock_report_service.called
