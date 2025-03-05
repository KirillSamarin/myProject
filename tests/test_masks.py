from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(number, number_zero, number_nine, short_number):
    assert get_mask_card_number(number) == "6853 72** **** **** 5446"
    assert get_mask_card_number(number_zero) == "0000 00** **** **00 00"
    assert get_mask_card_number(number_nine) == "9999 99** **** ***9 999"
    assert get_mask_card_number(short_number) == "563"
    assert get_mask_card_number("") == ""

def test_get_mask_account(number, number_zero, number_nine, short_number):
    assert get_mask_account(number) == "**5446"
    assert get_mask_account(number_zero) == "**0000"
    assert get_mask_account(number_nine) == "**9999"
    assert get_mask_account(short_number) == "**563"
    assert get_mask_account("") == "**"
