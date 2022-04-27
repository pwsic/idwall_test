from app.models.customer import CustomerModel
from app.repository.base import BaseRepository


class CustomerRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, CustomerModel)
