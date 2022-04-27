from flask_restx import Namespace, Resource

from app.services.history import HistoryService

history_api = Namespace('history', 'History')


@history_api.route("/")
class History(Resource):
    def get(self):
        service = HistoryService()
        service.get_history_by_period('sss', 'hhhh')
        return {'oi': 'hey'}
