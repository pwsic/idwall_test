from app.common.exceptions import CustomerNotFoundException
from app.repository.customer import CustomerRepository


class CustomerService:
    def __init__(self, session):
        self.repository = CustomerRepository(session)

    def get_by_id(self, id_):
        resource = self.repository.get_by_id(id_)
        if not resource:
            raise CustomerNotFoundException
        return resource
