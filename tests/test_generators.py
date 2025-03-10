from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
import pytest


def test_filter_by_currency(transactions):
    transactions_filtered = filter_by_currency(transactions, "USD")
    assert next(transactions_filtered) == {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                                           'operationAmount': {'amount': '9824.07',
                                                               'currency': {'name': 'USD', 'code': 'USD'}},
                                           'description': 'Перевод организации',
                                           'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}

    transactions_filtered = filter_by_currency([], "")
    assert next(transactions_filtered) == "Список не должен быть пустым"

    transactions_filtered = filter_by_currency([], "USD")
    assert next(transactions_filtered) == "Список не должен быть пустым"

    transactions_filtered = filter_by_currency(transactions, "EUR")
    assert next(transactions_filtered) == "Транзакций с этой валютой нет в списке"


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"

    descriptions = transaction_descriptions([])
    assert next(descriptions) == "Список не должен быть пустым"

    descriptions = transaction_descriptions((transactions[0:4]))
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"


@pytest.mark.parametrize("start_number, end_number, result", [(1, 5, "0000 0000 0000 0001"),
                                                              (3, 9, "0000 0000 0000 0003"),
                                                              (0000000000000000, 9999999999999999,
                                                               "0000 0000 0000 0000")])
def test_card_number_generator(start_number, end_number, result):
    card_number = card_number_generator(start_number, end_number)
    assert next(card_number) == result
