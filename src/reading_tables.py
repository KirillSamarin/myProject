import pandas as pd


def dict_csv(path: str):
    csv_dicts = []
    with open(path, encoding="utf-8") as file:
        reader = pd.read_csv(file, delimiter=";")
        for line in range(reader.shape[0]):
            csv_dicts.append(dict(reader.iloc[line]))
    return csv_dicts


def dict_excel(path: str):
    xlsx_dicts = []
    df = pd.read_excel(path, engine='openpyxl')
    for line in range(df.shape[0]):
        xlsx_dicts.append(dict(df.iloc[line]))
    return xlsx_dicts
