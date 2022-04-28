from app.models.request_history import RequestHistoryModel
from app.repository.request_history import RequestHistoryRepository
from app.services.partner_bank import PartnerBankService


class RequestHistoryService:
    def __init__(self, session):
        self.repository = RequestHistoryRepository(session)

    def get(self, id_):
        return self.repository.get_by_id(id_)

    def create(self, payload):
        return self.repository.create(RequestHistoryModel(**payload))

    def update(self, payload, id_):
        return self.repository.update(payload, id_)

    @staticmethod
    def get_history_by_period(customer_id, initial_date, end_date):
        service = PartnerBankService()
        return service.get_history_by_period(customer_id, initial_date, end_date)

    # NESTE CASO, NÃO ME PREOCUPEI COM O TAMANHO DO BANCO, APENAS EM PEGAR AS MENSAGENS PARA TESTAR O FLUXO
    def get_all_requests_with_error(self):
        return self.repository.get_all_with_error()
