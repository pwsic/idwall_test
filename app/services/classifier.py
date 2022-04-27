from datetime import datetime

from app.services.suspicious_transaction import SuspiciousTransactionService


class ClassifierService:
    """
    A ideia aqui seria a seguinte:.

    Consultar na tabela purchase history se determinado cliente
    possui uma ou mais compras em determinada categoria.

    Se não possuir compra nessa categoria (conforme simulado na linha 12), salvar como uma transação suspeita
    Caso contrario, seguir o fluxo normalmente
    """

    def __init__(self, session):
        self.service = SuspiciousTransactionService(session)

    def classify(self, payload):
        for transaction in payload["expenses"]:
            if transaction["categoryId"] == "3f1dbe6b-fddd-40e6-bfc4-aaf6e6cda430":
                suspicious_payload = {
                    "category_id": transaction["categoryId"],
                    "purchase_id": transaction["purchaseId"],
                    "money_spent": transaction["moneySpent"],
                    "purchase_date": datetime.now(),  # criado chumbado apenas para não parsear data
                    "customer_id": payload["id"],
                }
                self.service.create(suspicious_payload)

        return payload
