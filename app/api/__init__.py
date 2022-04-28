from flask_restx import Api

from app.api.history.views import history_api
from app.api.report.views import report_api

api = Api(
    title="IdWall - Swagger Bacaninha",
    version="1.0",
    description="History Api",
)

api.add_namespace(history_api)
api.add_namespace(report_api)
