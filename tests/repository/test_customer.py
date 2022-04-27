
from app.models.base import session
from app.repository.customer import CustomerRepository


class TestRepositoryCustomer:
    def test_get_user_should_return_one_result(self, app, fixture_customer):
        repository = CustomerRepository(session)
        user = repository.get_by_id(fixture_customer.id)
        assert user is not None

    def test_get_user_should_return_none_result(self, app):
        repository = CustomerRepository(session)
        user = repository.get_by_id("bla")
        assert user is None
