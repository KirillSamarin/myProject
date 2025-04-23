import json
"""import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("..\\logs\\utils.log", "a", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel("INFO")"""


def json_read(path: str):
    """Получает на вход путь к файлу json, после чего возвращает его содержимое как объект python"""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        return []
