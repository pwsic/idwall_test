from app.common.exceptions import PartnerBankTimemoutException
from app.models.base import session
from app.services.classifier import ClassifierService
from app.services.report import ReportService
from app.services.request_history import RequestHistoryService
from celery_app import celery_app


@celery_app.task(queue="history")
def track_history(id_):
    report_service = ReportService(session)
    request_history_service = RequestHistoryService(session)
    request_history = request_history_service.get(id_)

    status = {"status": "success"}
    response = {}

    try:
        transactions = request_history_service.get_history_by_period(
            request_history.customer_id,
            request_history.initial_date,
            request_history.end_date,
        )

        classifier_service = ClassifierService(session)
        classified_transactions = classifier_service.classify(transactions)

        report = report_service.create(classified_transactions, request_history.id)
        response.update({'id': report.id})
    except (PartnerBankTimemoutException, Exception):
        status = {"status": "error"}

    request_history_service.update(status, id_)
    return response
