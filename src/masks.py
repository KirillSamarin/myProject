def get_mask_card_number(card_number: int) -> str:
    """Маскирует номер карты"""
    card_number = list(str(card_number))
    for index in range(6, 12):
        card_number[index] = "*"
    card_number.insert(4, " ")
    card_number.insert(9, " ")
    card_number.insert(14, " ")
    card_number = "".join(card_number)
    return card_number


def get_mask_account(account_number: int) -> str:
    """Маскирует номер счета"""
    return f"**{str(account_number)[-4:]}"

