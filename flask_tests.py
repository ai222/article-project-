import pytest


@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()
