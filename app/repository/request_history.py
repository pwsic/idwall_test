from sqlalchemy import select

from app.models.request_history import RequestHistoryModel
from app.repository.base import BaseRepository


class RequestHistoryRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, RequestHistoryModel)

    def get_all_with_error(self):
        query = select(RequestHistoryModel).where(RequestHistoryModel.status == 'error')
        results = self.session.execute(query)
        return results.scalars().all()
