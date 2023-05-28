import pytest
from utils import validate_data

@pytest.mark.parametrize('transactions, expected',[
    ([
        {
            "id":441945886,
            "state":"EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "id": 41428829,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",

        }
    ],
    [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",

        }
    ])
])


def test_validate_data(transactions, expected):
    assert validate_data.keep_executed(transactions) == expected


@pytest.mark.parametrize('transactions, expected',[
    ([
        {
            "id":441945886,
            "state":"EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "id": 41428829,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",

        }
    ],
    [0, 1])
])


def test_get_latest_transaction_numbers(transactions, expected):
    assert validate_data.get_latest_transaction_numbers(transactions) == expected


@pytest.mark.parametrize('transactions, numbers, expected',[
    ([
        {
            "id":441945886,
            "state":"EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "id": 41428829,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",

        }
    ],
    [0],
    [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",

        }
    ])
])

def test_get_latest_transactions(transactions, numbers, expected):
    assert validate_data.get_latest_transactions(transactions, numbers) == expected