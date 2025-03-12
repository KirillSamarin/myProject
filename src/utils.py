import json


def json_read(path):
    """Получает на вход путь к файлу json, после чего возвращает его содержимое как объект python"""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception:
        return []
