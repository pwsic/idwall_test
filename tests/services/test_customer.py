import pytest

from app.common.exceptions import CustomerNotFoundException
from app.models.base import session
from app.services.customer import CustomerService


class TestCustomerService:
    def test_get_customer_should_return_result(self, app, fixture_customer):
        service = CustomerService(session)
        customer = service.get_by_id(fixture_customer.id)

        assert customer is not None

    def test_get_report_should_return_raise_exception_due_not_found_resource(self, app):
        service = CustomerService(session)

        with pytest.raises(CustomerNotFoundException):
            service.get_by_id("aslkdfalsjdf")
