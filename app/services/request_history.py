from app.models.request_history import RequestHistoryModel
from app.repository.request_history import RequestHistoryRepository


class RequestHistoryService:
    def __init__(self, session):
        self.repository = RequestHistoryRepository(session)

    def create(self, payload):
        return self.repository.create(RequestHistoryModel(**payload))
