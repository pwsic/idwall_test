import random
from uuid import uuid4

from app.common.exceptions import PartnerBankTimemoutException


def mock_success_response(customer_id):
    expenses = {
        "id": customer_id,
        "expenses": [
            {
                "categoryId": "00e88809-e3df-4e6a-9351-9c74b239649b",
                "categoryName": "Serviços Automotivos",
                "purchaseId": str(uuid4()),
                "moneySpent": 150,
                "purchaseDate": "25/12/2021",
            },
            {
                "categoryId": "224e56e6-0c88-4a3d-b05c-f349ebd5f187",
                "categoryName": "Vestuário",
                "purchaseId": str(uuid4()),
                "moneySpent": 150,
                "purchaseDate": "25/12/2021",
            },
        ],
    }

    if customer_id == "17d16d56-4802-43fb-a502-0cd504ec4523":
        expenses["expenses"].append(
            {
                "categoryId": "3f1dbe6b-fddd-40e6-bfc4-aaf6e6cda430",
                "categoryName": "Categoria muito suspeita",
                "purchaseId": str(uuid4()),
                "moneySpent": 150,
                "purchaseDate": "25/12/2021",
            }
        )

    return expenses


class PartnerBankService:
    def get_history_by_period(self, customer_id, initial_date, end_date):
        if random.randint(1, 3) == 2:
            raise PartnerBankTimemoutException

        return mock_success_response(customer_id)
