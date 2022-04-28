from app.models.suspicious_transaction import SuspiciousTransactionModel
from app.repository.base import BaseRepository


class SuspiciousTransactionRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, SuspiciousTransactionModel)
