from fastapi.testclient import TestClient
from src.schemes.schemes import DepositIn, ErrorMessages
from src.api.calculation import calculations
from src.main import app

client = TestClient(app)

ENDPOINT = '/api/calculate-deposit/'


def test_calculate_deposit():
    data = DepositIn(date="31.01.2021", periods=3, amount=10000, rate=6)
    result = calculations(data)
    expected_result = {
        "31.01.2021": 10050.0,
        "28.02.2021": 10100.25,
        "31.03.2021": 10150.75
    }
    assert result.results == expected_result


def test_calculate_deposit_valid():
    data = {"date": "31.01.2021", "periods": 3, "amount": 10000, "rate": 6}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == 200
    assert response.json() == {"results": {"31.01.2021": 10050.0, "28.02.2021": 10100.25, "31.03.2021": 10150.75}}


def test_calculate_deposit_invalid_rate():
    data = {"date": "31.01.2021", "periods": 3, "amount": 10000, "rate": 10}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == 400
    assert response.json() == {"detail": ErrorMessages.RATE_ERROR.value}


def test_calculate_deposit_invalid_periods():
    data = {"date": "31.01.2021", "periods": 61, "amount": 10000, "rate": 6}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == 400
    assert response.json() == {"detail": ErrorMessages.PERIOD_ERROR.value}


def test_calculate_deposit_invalid_amount():
    data = {"date": "31.01.2021", "periods": 3, "amount": 4000000, "rate": 6}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == 400
    assert response.json() == {"detail": ErrorMessages.AMOUNT_ERROR.value}
