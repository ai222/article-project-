from app import home
from caculator import Calculator
import pytest
from flask import Flask


# These are below to test the calculator

def calculator_is_instance():
    """Testing the Calculator"""
    calculator = Calculator(1, 2)
    assert isinstance(calculator, Calculator)


def calculator_result_property():
    """Testing the Calculator"""
    calc1 = Calculator(1, 2)
    calc2 = Calculator(3, 4)
    calc1.result = 5
    calc2.result = 6
    assert calc1.result == 5
    assert calc2.result == 6


def calculator_add_method():
    """Testing the Calculator"""
    calculator = Calculator(1, 1)
    assert calculator.add() == 2


def calculator_subtract_method():
    """Testing the Calculator Subtract"""
    calculator = Calculator(2, 2)
    assert calculator.subtract() == 0


def test_home():
    assert home() == "Hello World"


"""This test the homepage"""


def request_index():
    """This makes the index page"""
    app = Flask(__name__)
    client = app.test_client()
    url = "/"
    response = client.get(url)
    assert response.status_code == 404


def request_git():
    """This makes the index page"""
    app = Flask(__name__)
    client = app.test_client()
    url = "/git"
    response = client.get(url)
    assert response.status_code == 404


def request_docker():
    """This makes the index page"""
    app = Flask(__name__)
    client = app.test_client()
    url = "/docker"
    response = client.get(url)
    assert response.status_code == 404


def request_oop():
    """This makes the index page"""
    app = Flask(__name__)
    client = app.test_client()
    url = "/oop"
    response = client.get(url)
    assert response.status_code == 404


def request_topic():
    """This makes the index page"""
    app = Flask(__name__)
    client = app.test_client()
    url = "/topics"
    response = client.get(url)
    assert response.status_code == 404


def request_cicd():
    """This makes the index page"""
    app = Flask(__name__)
    client = app.test_client()
    url = "/cicd"
    response = client.get(url)
    assert response.status_code == 404
