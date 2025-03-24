from re import sub
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("..\\logs\\masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel("INFO")


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты"""
    logger.info("Фукнция get_mask_card_number вызвана")
    if not card_number:
        logger.info("успешное выполнение фукнции")
        return ""

    if len(card_number) <= 10:
        masked_part_len = max(0, len(card_number) - 4)
        masked_part = "*" * masked_part_len
        masked_card_number = masked_part + card_number[-4:]
    else:
        masked_part = "*" * len(card_number[6:-4])
        masked_card_number = card_number[:6] + masked_part + card_number[-4:]

    formatted_card_number = sub("(.{4})", r"\1 ", masked_card_number)
    logger.info("успешное выполнение функции")
    return formatted_card_number.strip()


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета"""
    logger.info("функция get_mask_account вызвана")
    logger.info("успешное выполнение функции")
    return f"**{account_number[-4:]}"
