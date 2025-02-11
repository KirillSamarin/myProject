def filter_by_state(dicts, state="EXECUTED"):
    dicts_to_return = []
    for elem in dicts:
        if elem["state"] == state:
            dicts_to_return.append(elem)
    return dicts_to_return

