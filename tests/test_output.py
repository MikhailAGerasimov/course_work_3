import pytest
from utils import output


@pytest.mark.parametrize('transactions',[
    (
    [
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
    }])
])

def test_output_transactions1(transactions, capsys):
    output.output_transactions(transactions)
    captured = capsys.readouterr()
    assert captured.out == "26.08.19 Перевод организации\nMaestro 1596** **** 5199 -> Счет **9589\n31957.58 руб.\n\n"


@pytest.mark.parametrize('transactions',[
    ([
        {
            "id": 147815167,
            "state": "EXECUTED",
            "date": "2018-01-26T15:40:13.413061",
            "operationAmount": {
                "amount": "50870.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 4598300720424501",
            "to": "Счет 43597928997568165086"
        }
    ]

    )
])

def test_output_transactions2(transactions, capsys):
    output.output_transactions(transactions)
    captured = capsys.readouterr()
    assert captured.out == "26.01.18 Перевод с карты на счет\nMaestro 4598** **** 4501 -> Счет **5086\n50870.71 руб.\n\n"


@pytest.mark.parametrize('transactions',[
    ([
        {
            "id": 172864002,
            "state": "EXECUTED",
            "date": "2018-12-28T23:10:35.459698",
            "operationAmount": {
                "amount": "49192.52",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 96231448929365202391"
        }
    ]

    )
])

def test_output_transactions3(transactions, capsys):
    output.output_transactions(transactions)
    captured = capsys.readouterr()
    assert captured.out == "28.12.18 Открытие вклада\nСчет **2391\n49192.52 USD\n\n"


@pytest.mark.parametrize('transactions',[
    ([
        {
            "id": 888407131,
            "state": "EXECUTED",
            "date": "2019-09-29T14:25:28.588059",
            "operationAmount": {
                "amount": "45849.53",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 35421428450077339637",
            "to": "Счет 46723050671868944961"
        }
    ]

    )
])

def test_output_transactions4(transactions, capsys):
    output.output_transactions(transactions)
    captured = capsys.readouterr()
    assert captured.out == "29.09.19 Перевод со счета на счет\nСчет **9637 -> Счет **4961\n45849.53 USD\n\n"


@pytest.mark.parametrize('transactions',[
    (
    [
        {
            "id": 34148726,
            "state": "EXECUTED",
            "date": "2018-11-23T23:52:36.999661",
            "operationAmount": {
                "amount": "79428.73",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 5355133159258236",
            "to": "Maestro 8045769817179061"
        }])
])

def test_output_transactions5(transactions, capsys):
    output.output_transactions(transactions)
    captured = capsys.readouterr()
    assert captured.out == "23.11.18 Перевод с карты на карту\nVisa Platinum 5355** **** 8236 -> Maestro 8045** **** 9061\n79428.73 USD\n\n"