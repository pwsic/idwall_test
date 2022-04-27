import pytest
from sqlalchemy import select

from app.models.base import session
from app.models.category import CategoryModel
from app.models.customer import CustomerModel
from app.models.suspicious_transaction import SuspiciousTransactionModel
from app.services.classifier import ClassifierService
from app.services.partner_bank import mock_success_response


class TestClassifierService:
    @pytest.fixture()
    def fixture_customer_with_suspicious_category(self):
        customer = CustomerModel(
            id="17d16d56-4802-43fb-a502-0cd504ec4523", name="flavinho flaveta"
        )
        session.add(customer)
        session.commit()

        return customer

    @pytest.fixture()
    def fixture_category(self):
        customer = CategoryModel(
            id="3f1dbe6b-fddd-40e6-bfc4-aaf6e6cda430", name="Suspeitosa"
        )
        session.add(customer)
        session.commit()

        return customer

    def test_classify_should_classify_and_create_suspicious_transaction(
        self, app, fixture_customer_with_suspicious_category, fixture_category
    ):
        before_create = session.execute(
            select(SuspiciousTransactionModel).where(
                SuspiciousTransactionModel.customer_id
                == fixture_customer_with_suspicious_category.id
            )
        )
        before_create = before_create.scalars().all()
        assert len(before_create) == 0

        transactions = mock_success_response(
            fixture_customer_with_suspicious_category.id
        )

        service = ClassifierService(session)
        service.classify(transactions)

        after_create = session.execute(
            select(SuspiciousTransactionModel).where(
                SuspiciousTransactionModel.customer_id
                == fixture_customer_with_suspicious_category.id
            )
        )
        after_create = after_create.scalars().all()
        assert len(after_create) == 1
