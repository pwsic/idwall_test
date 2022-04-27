from flask_restx import Api

from app.api.history.views import history_api

api = Api(
    title="My Title",
    version="1.0",
    description="History Api",
)


api.add_namespace(history_api)
