import pytest

@pytest.fixture
def number():
    return "68537238237002905446"

@pytest.fixture
def number_zero():
    return "000000000000000000"

@pytest.fixture
def number_nine():
    return "9999999999999999999"

@pytest.fixture
def short_number():
    return "563"

@pytest.fixture
def text():
    return "aaaaaa"

@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"

@pytest.fixture
def no_state():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def same_dates():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
                         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def incorrect_dates():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': 'hsgia'},
                         {'id': 939719570, 'state': 'EXECUTED', 'date': 'kjsd'},
                         {'id': 594226727, 'state': 'CANCELED', 'date': 'sjhd'},
                         {'id': 615064591, 'state': 'CANCELED', 'date': ''}]

@pytest.fixture
def dates():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
