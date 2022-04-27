from datetime import datetime

from sqlalchemy import select

from app.models.base import session
from app.models.request_history import RequestHistoryModel
from app.repository.request_history import RequestHistoryRepository


class TestRepositoryRequestHistory:
    def test_create_should_work(self, app, fixture_customer):
        before_create = session.execute(select(RequestHistoryModel))
        before_create = before_create.scalars().all()
        assert len(before_create) == 0

        model = RequestHistoryModel(
            **{
                "customer_id": fixture_customer.id,
                "initial_date": datetime.now(),
                "end_date": datetime.now(),
                "status": "init",
            }
        )

        repository = RequestHistoryRepository(session)
        request_history = repository.create(model)
        assert request_history is not None

        after_create = session.execute(select(RequestHistoryModel))
        after_create = after_create.scalars().all()
        assert len(after_create) == 1
