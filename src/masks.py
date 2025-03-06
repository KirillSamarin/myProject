from re import sub


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты"""
    if not card_number:
        return ""

    if len(card_number) <= 10:
        masked_part_len = max(0, len(card_number) - 4)
        masked_part = "*" * masked_part_len
        masked_card_number = masked_part + card_number[-4:]
    else:
        masked_part = "*" * len(card_number[6:-4])
        masked_card_number = card_number[:6] + masked_part + card_number[-4:]

    formatted_card_number = sub("(.{4})", r"\1 ", masked_card_number)
    return formatted_card_number.strip()


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета"""
    return f"**{account_number[-4:]}"
