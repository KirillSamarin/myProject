Библиотека для работы с финансами и счетами

Установка
Перед установкой должны быть установлены все зависимости, указанные в файле pyproject.toml

1. установить можно простым клонированием репозитория в консоли: git clone https://github.com/KirillSamarin/myProject.git, 
после чего все нужные модули будут доступны в пакете src

Функции и их примеры использования

masks.py

get_mask_card_number(7000792289606361)
Возвращает: 7000 79** **** 6361  

get_mask_account(73654108430135874305)
Возвращает: **4305

widget.py

Пример для с номером карты
mask_account_card("Visa Platinum 7000792289606361")
Возвращает: Visa Platinum 7000 79** **** 6361 

Пример с номером счета
mask_account_card("Счет 73654108430135874305")
Возвращает: **4305

get_date("2024-03-11T02:26:18.671407")
Возвращает: 11.03.2024

processing.py

filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], state="CANCELED")
Возвращает: [{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]

sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], reverse=False)
Возвращает:  [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

generators.py

transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }

transactions_filtered = filter_by_currency(transactions, "USD")

next(transactions_filtered) вовзвращает: {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                                           'operationAmount': {'amount': '9824.07',
                                                               'currency': {'name': 'USD', 'code': 'USD'}},
                                           'description': 'Перевод организации',
                                           'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}

descriptions = transaction_descriptions(transactions)

next(descriptions) возвращает: "Перевод организации"

card_number = card_number_generator(1, 5)

next(card_number) возвращает: "0000 0000 0000 0001"

decorators.py

декоратора log логирует функцию в консоль либо в файл:
function ok - успешное выполнение
function error: имя ошибки Inputs: (), {} - ошибка при выполнении, где имя ошибки - исключение, которое вызвало ошибку(TypeError, NameError и т.д)

Пример

@log()
def add_numbers(a, b):
    return a + b
add_numbers(1, 2)
возвращает: "add_numbers ok"

@log("logs")
def add_numbers(a, b):
    return a + b
add_numbers(1, 2)
В файле: "add_numbers ok\n"(перенос строки для корректного вида строк на экране)

utils.py

json_file
{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

read_json("json_file")
Возвращает: {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

external_api.py

retun_amount_rub({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  })

Возвращает: 31957.58

reading_tables.py

dict_csv("..\data\\transactions.csv") - указываем путь к файлу в качества аргумента
Возвращает: [{'id': np.float64(650703.0), 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': np.float64(16210.0), 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}, {'id': np.float64(3598919.0), 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': np.float64(29740.0), 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}...]
Аналогично и с функцией dict_excel()

Тесты

Функции проходят все тесты успешно, покрытие кода составляет 100%, подтверждение и дополнительная информация в index.html в папке htmlcov

