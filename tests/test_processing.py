from src.processing import filter_by_state, sort_by_date
import pytest

@pytest.mark.parametrize("lists, state, result", [([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], "EXECUTED",
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
            ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], "CANCELED", []),
            ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'}], "EXECUTED",
             [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])])
def test_filter_by_state(no_state, lists, state, result):
    assert filter_by_state(no_state, "a") == []
    assert filter_by_state(lists, state) == result

def test_sort_by_date(same_dates, incorrect_dates, dates):
    assert sort_by_date(same_dates) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
                                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'}]

    assert sort_by_date(incorrect_dates) == [{'id': 594226727, 'state': 'CANCELED', 'date': 'sjhd'},
                                             {'id': 939719570, 'state': 'EXECUTED', 'date': 'kjsd'},
                                             {'id': 41428829, 'state': 'EXECUTED', 'date': 'hsgia'},
                                             {'id': 615064591, 'state': 'CANCELED', 'date': ''}]

    assert sort_by_date(dates) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

    assert sort_by_date(dates, reverse=False) == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                                  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
