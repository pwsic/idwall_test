from app.models.base import session
from app.services.request_history import RequestHistoryService
from app.tasks.history import track_history
from celery_app import celery_app


@celery_app.task(queue="reprocess")
def reprocess():
    service = RequestHistoryService(session)
    with_error = service.get_all_requests_with_error()

    for item in with_error:
        track_history.delay(item.id)

    return {}
