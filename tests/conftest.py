from datetime import datetime

import pytest

from app import create_app
from app.models.base import Base, session
from app.models.category import CategoryModel
from app.models.customer import CustomerModel
from app.models.report import ReportModel
from app.models.request_history import RequestHistoryModel


@pytest.fixture()
def app():
    from app.models.base import engine, session

    global connection

    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    connection = engine.connect()
    Base.session = session
    Base.metadata.bind = engine

    Base.metadata.create_all()
    yield app
    Base.metadata.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture()
def fixture_customer():
    customer = CustomerModel(name="flavinho flaveta")
    session.add(customer)
    session.commit()

    return customer


@pytest.fixture()
def fixture_category():
    model = CategoryModel(id="3f1dbe6b-fddd-40e6-bfc4-aaf6e6cda430", name="Suspeitosa")
    session.add(model)
    session.commit()

    return model


@pytest.fixture()
def fixture_request_history(fixture_customer):
    model = RequestHistoryModel(
        customer_id=fixture_customer.id,
        initial_date=datetime.now(),
        end_date=datetime.now(),
        status="success",
    )
    session.add(model)
    session.commit()

    return model


@pytest.fixture()
def fixture_report(fixture_request_history):
    model = ReportModel(
        customer_id=fixture_request_history.customer_id,
        request_history_id=fixture_request_history.id,
        expenses=[
            {
                "categoryId": "3f1dbe6b-fddd-40e6-bfc4-aaf6e6cda430",
                "categoryName": "Categoria muito suspeita",
                "purchaseId": "5852769a-9e1e-41cb-8d26-9a8bfb33fcd4",
                "moneySpent": 150,
                "purchaseDate": "25/12/2021",
            }
        ],
    )
    session.add(model)
    session.commit()

    return model
