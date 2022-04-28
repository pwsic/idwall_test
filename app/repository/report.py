from app.models.report import ReportModel
from app.repository.base import BaseRepository


class ReportRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, ReportModel)
