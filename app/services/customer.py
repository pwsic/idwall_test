from app.api.history.exceptions import CustomerNotFoundException
from app.repository.customer import CustomerRepository


class CustomerService:
    def __init__(self, session):
        self.repository = CustomerRepository(session)

    def get_customer_by_id(self, id):
        customer = self.repository.get_by_id(id)
        if not customer:
            raise CustomerNotFoundException
        return customer
