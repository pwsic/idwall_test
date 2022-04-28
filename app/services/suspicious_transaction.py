from app.models.category import CategoryModel
from app.models.suspicious_transaction import SuspiciousTransactionModel
from app.repository.suspicious_transaction import SuspiciousTransactionRepository


class SuspiciousTransactionService:
    def __init__(self, session):
        self.repository = SuspiciousTransactionRepository(session)

    def create(self, payload):
        model = SuspiciousTransactionModel(**payload)
        return self.repository.create(model)
