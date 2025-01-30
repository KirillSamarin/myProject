from masks import get_mask_account, get_mask_card_number

def mask_account_card(account_card_number: str) -> str:
    """Принимает номер счета или карты, а затем маскирует"""
    account_card_number = account_card_number.split()
    if "счет" in account_card_number[0].lower():
        account_card_number[-1] = get_mask_account(int(account_card_number[-1]))
    else:
        account_card_number[-1] = get_mask_card_number(int(account_card_number[-1]))
    return " ".join(account_card_number)

def get_date(date: str) -> str:
    """Принимает строку в формате 2024-03-11T02:26:18.671407 и возвращает из нее дату в формате ДД.ММ.ГГГГ(11.03.2024)"""
    date = date[0:10].split("-")
    return ".".join(date[::-1])

