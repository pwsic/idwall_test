from flask import request
from flask_restx import Namespace, Resource, abort

from app.api.history.schema import history_post_schema
from app.common.exceptions import CustomerNotFoundException
from app.models.base import session
from app.services.customer import CustomerService
from app.tasks.history import track_history

history_api = Namespace("history", "History")

resource_fields = history_api.model("Resource", history_post_schema)


@history_api.route("/")
class History(Resource):
    @history_api.doc(body=resource_fields)
    def post(self):
        track_history.delay("34a52148-64fe-4cc8-af37-624aba5909a9")

        try:
            payload = request.json
            customer_service = CustomerService(session)
            customer_service.get_customer_by_id(payload["id"])

            # criar serviço do worker aqui (criação de fila para consumo - request history)
        except CustomerNotFoundException:
            abort(404, "Customer not found")
        except Exception:
            pass
        return {"oi": "hey"}
