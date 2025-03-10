from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize("type_number, masked", [("Visa Platinum 7000792289606361",
                                                  "Visa Platinum 7000 79** **** 6361"),
                                                 ("Счет 73654108430135874305", "Счет **4305"),
                                                 ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
                                                 ("7000792289606361", "7000 79** **** 6361")])
def test_mask_card_account(type_number, masked):
    assert mask_account_card(type_number) == masked


def test_get_date(date, text):
    assert get_date(date) == "11.03.2024"
    assert get_date(text) == "Введите данные в корректном формате"
    assert get_date("") == "Введите данные в корректном формате"
    assert get_date("03 11 2024") == "11.03.2024"
