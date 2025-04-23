import re
from collections import Counter


def filter_dicts(dicts: list[dict], search_string: str) -> list[dict]:
    filtered_dicts = []

    for d in dicts:
        if "description" in d and re.search(search_string, d["description"], re.IGNORECASE):
            filtered_dicts.append(d)

    return filtered_dicts


def dicts_by_categories(dicts: list[dict], categories: list[str]) -> dict:
    categories = [c.lower() for c in categories]
    descriptions = []

    for d in dicts:
        if "description" in d and d["description"].lower() in categories:
            descriptions.append(d["description"].lower())

    counter = Counter(descriptions)

    result = {}
    for category in categories:
        result[category] = counter.get(category, 0)
    return result
