from datetime import datetime, time

from flask import request
from flask_restx import Namespace, Resource, abort

import settings
from app.api.history.schema import history_post_schema
from app.common.exceptions import CustomerNotFoundException
from app.models.base import session
from app.services.customer import CustomerService
from app.services.request_history import RequestHistoryService
from app.tasks.history import track_history

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

            initial_date = datetime.strptime(payload['initialDate'], '%d/%m/%Y')
            end_date = datetime.strptime(payload['finalDate'], '%d/%m/%Y')

            request_history_payload = {
                'customer_id': payload['id'],
                'initial_date': datetime.combine(initial_date.date(), time(0, 0, 0)),
                'end_date': datetime.combine(end_date.date(), time(23, 59, 59)),
                'status': 'init',
            }

            request_history_service = RequestHistoryService(session)
            request_history = request_history_service.create(request_history_payload)
            response = {
                'request_history': request_history.id
            }

            # TODO mockar e testar isso aqui
            if 'memory' not in settings.get("sqlalchemy.url"):
                track_history.delay(request_history.id)

        except CustomerNotFoundException:
            abort(404, "Customer not found")
        return response
