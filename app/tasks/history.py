from app.models.base import session
from app.repository.customer import CustomerRepository
from celery_app import celery_app


@celery_app.task(queue="history")
def track_history(id_):
    """
    criar serviço de atualizaçao de mensagem

    criar serviço de classificação de mensagem

    """

    # TODO REFACTOR THIS
    repository = CustomerRepository(session)
    customer = repository.get_by_id(id_)
    print('@@@@@@@@@@@@@@@@@@@@@@@')
    print(customer)
    print('@@@@@@@@@@@@@@@@@@@@@@@')



"""

"""
