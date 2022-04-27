import pytest

from app import create_app
from app.models.base import Base


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
