import datetime


def output_transactions(transactions):
    """
    Вывод списка транакций в требуемом формате
    :param transactions: список транзакций
    :return: None
    """
    for elem in transactions:
        date = elem.get('date')
        date = date.replace('T', ' ')
        date_format = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        print(f'{date_format.strftime("%d.%m.%y")} {elem["description"]}')
        if elem['description'] == 'Перевод с карты на счет':
            print(f'{output_card(elem["from"])} -> {output_account(elem["to"])}')
        elif elem['description'] == 'Открытие вклада':
            print(f'{output_account(elem["to"])}')
        elif elem['description'] == 'Перевод организации':
            print(f'{output_card(elem["from"])} -> {output_account(elem["to"])}')
        elif elem['description'] == 'Перевод со счета на счет':
            print(f'{output_account(elem["from"])} -> {output_account(elem["to"])}')
        elif elem['description'] == 'Перевод с карты на карту':
            print(f'{output_card(elem["from"])} -> {output_card(elem["to"])}')
        print(f'{elem["operationAmount"]["amount"]} {elem["operationAmount"]["currency"]["name"]}\n')


def output_card(card_num):
    """
    Функция преобразования номера карты в зашифрованный вид
    :param card_num: номер карты
    :return: номер карты в зашифрованном виде
    """
    return (card_num[:-5:-1] + " **** **" + card_num[-13::-1])[::-1]


def output_account(acc_num):
    """
    Функция преобразования номера счета в зашифрованный вид
    :param acc_num: номер счета
    :return: номер счета в зашифрованном виде
    """
    return "Счет **" + acc_num[-4:]