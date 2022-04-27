from app.models.report import ReportModel
from app.repository.report import ReportRepository


class ReportService:
    def __init__(self, session):
        self.repository = ReportRepository(session)

    def create(self, payload, request_history_id):
        model = ReportModel(
            customer_id=payload['id'],
            expenses=payload['expenses'],
            request_history_id=request_history_id
        )
        return self.repository.create(model)
