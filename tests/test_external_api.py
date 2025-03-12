from unittest import mock
from src.external_api import return_amount_rub


def test_currency_rub():
    transaction_rub = {
        "operationAmount": {
            "currency": {"code": "RUB"},
            "amount": 100.0
        }
    }
    result = return_amount_rub(transaction_rub)
    assert result == 100.0


def test_currency_usd_successful_api():
    transaction_usd = {
        "operationAmount": {
            "currency": {"code": "USD"},
            "amount": 10.0
        }
    }
    with mock.patch('src.external_api.requests.get') as mock_get:
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 800.0}
        mock_get.return_value = mock_response

        result = return_amount_rub(transaction_usd)
        assert result == 800.0
        mock_get.assert_called_once()


def test_currency_eur_successful_api():
    transaction_eur = {
        "operationAmount": {
            "currency": {"code": "EUR"},
            "amount": 5.0
        }
    }
    with mock.patch('src.external_api.requests.get') as mock_get:
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 1000.0}
        mock_get.return_value = mock_response

        result = return_amount_rub(transaction_eur)
        assert result == 1000.0
        mock_get.assert_called_once()
