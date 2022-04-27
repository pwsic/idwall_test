from app.models.request_history import RequestHistoryModel
from app.repository.base import BaseRepository


class RequestHistoryRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, RequestHistoryModel)
