import src.reading_tables
import src.utils
import src.generators
import src.processing
import src.dicts_sort
import src.widget

def main():
    print("""Программа: Привет! Добро пожаловать в программу работы 
    с банковскими транзакциями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла""")

    file = []

    user_input = input()

    if user_input == "1":
        print("Для обработки выбран JSON-файл.")
        file = src.utils.json_read(".\\data\\operations.json")
    elif user_input == "2":
        print("Для обработки выбран CSV-файл.")
        file = src.reading_tables.dict_csv(".\\data\\transactions.csv")
    elif user_input == "3":
        print("Для обработки выбран XLSX-файл.")
        file = src.reading_tables.dict_excel(".\\data\\transactions_excel.xlsx")

    print("""Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

    user_input = input()

    if not user_input.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {user_input} недоступен.")
    else:
        file = src.processing.filter_by_state(file, user_input.upper())

    print("Отсортировать операции по дате? Да/Нет")

    user_input = input()

    if user_input.lower() == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_input = input()
        if user_input.lower == "по возрастанию":
            file = src.processing.sort_by_date(file, reverse=False)
        else:
            file = src.processing.sort_by_date(file)

    print("Выводить только рублевые тразакции? Да/Нет")

    user_input = input()

    if user_input.lower() == "да":
        file = src.generators.filter_by_currency(file, "RUB")

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")

    user_input = input()

    if user_input.lower() == "да":
        print("Введите слово, по которому будет производиться поиск")
        user_input = input()
        file = src.dicts_sort.filter_dicts(file, user_input)

    print("Распечатываю итоговый список транзакций...")

    for transaction in file:
        to_from = f"{transaction["to"]}"
        if "from" in transaction.keys():
            transaction["from"] = src.widget.mask_account_card(str(transaction["from"]))
            to_from = f"{transaction["from"]} -> {transaction["to"]}"
        transaction["to"] = src.widget.mask_account_card(transaction["to"])
        transaction["date"] = src.widget.get_date(transaction["date"])
        print(f"{transaction["date"]} {transaction["description"]}")
        print(to_from)
        if "operationAmount" in transaction.keys():
            print(f"Сумма: {transaction["operationAmount"]["amount"]} {transaction["operationAmount"]["currency"]["code"]}")
        else:
            print(f"Сумма: {transaction["amount"]} {transaction["currency_code"]}")
main()
