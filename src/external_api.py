import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")
payload = {}
headers = {
    "apikey": API_KEY
}


def return_amount_rub(transaction: dict) -> float:
    """Получает на вход транзакцию в виде словаря, после чего возвращает ее сумму в рублях"""
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]

    if currency == "RUB":
        return amount

    if currency in ["USD", "EUR"]:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        response = requests.get(url, headers=headers, data=payload)
        data = response.json()
        return round(data["result"], 2)
