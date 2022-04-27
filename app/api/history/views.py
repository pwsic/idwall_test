from flask import request
from flask_restx import Namespace, Resource, abort

from app.api.history.exceptions import CustomerNotFoundException
from app.api.history.schema import history_post_schema
from app.models.base import session
from app.services.customer import CustomerService

history_api = Namespace("history", "History")

resource_fields = history_api.model("Resource", history_post_schema)


@history_api.route("/")
class History(Resource):
    @history_api.doc(body=resource_fields)
    def post(self):
        try:
            payload = request.json
            customer_service = CustomerService(session)
            customer_service.get_customer_by_id(payload["id"])
        except CustomerNotFoundException:
            abort(404, "Customer not found")
        except Exception:
            pass
        return {"oi": "hey"}
