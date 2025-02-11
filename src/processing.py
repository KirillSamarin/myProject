def filter_by_state(dicts, state="EXECUTED"):
    """Принимает список словарей в параметр dicts, после чего возвращает те словари, у которых значение state совпадает
    со значением одноименного параметра"""
    dicts_to_return = []
    for elem in dicts:
        if elem["state"] == state:
            dicts_to_return.append(elem)
    return dicts_to_return

def sort_by_date(dicts, reverse=True):
    """Принимает список словарей в параметр dicts, после чего возвращает его, отсортировав по дате. Значение параметра
    reverse показывает порядок сортировки: True - по убыванию, False - по возрастанию"""
    if reverse:
        return sorted(dicts, key=lambda elem: elem["date"], reverse=True)
    else:
        return sorted(dicts, key=lambda elem: elem["date"])
