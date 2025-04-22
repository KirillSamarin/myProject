from typing import Iterator, Generator

def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Возвращает транзакции, которые производились с указанной валютой."""
    for transaction in transactions:
        if "operationAmount" in transaction.keys():
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        else:
            if transaction["currency_code"] == currency:
                yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Принимает список трзнакций и возвращает их описания"""
    if not transactions:
        yield "Список не должен быть пустым"
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start_number: int, end_number: int) -> Generator[str, None, None]:
    """Генерирует номера карт от начального номера до конечно(от start_number до end_number соответственно)"""
    for i in range(start_number, end_number + 1):
        card_number = str(i).zfill(16)
        formatted_card_number = " ".join([card_number[j:j+4] for j in range(0, 16, 4)])
        yield formatted_card_number
