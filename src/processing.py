def filter_by_state(dicts: list, state: str="EXECUTED") -> list:
    """Принимает список словарей в параметр dicts, после чего возвращает те словари, у которых значение state совпадает
    со значением одноименного параметра"""
    dicts_to_return = []
    for elem in dicts:
        if elem["state"] == state:
            dicts_to_return.append(elem)
    return dicts_to_return


def sort_by_date(dicts: list, reverse: bool=True) -> list:
    """Принимает список словарей в параметр dicts, после чего возвращает его, отсортировав по дате. Значение параметра
    reverse показывает порядок сортировки: True - по убыванию, False - по возрастанию"""
    if reverse:
        return sorted(dicts, key=lambda elem: elem["date"], reverse=True)
    else:
        return sorted(dicts, key=lambda elem: elem["date"])

print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], reverse=False))