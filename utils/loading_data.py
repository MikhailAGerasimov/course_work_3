import json


def load_data(path):
    '''
    Фнукция получает на вход путь до файла с транзакциями
    и возвращает список словарей
    :param path: путь до файла
    :return: список словарей с транзакциями
    '''
    with open(path, encoding='utf-8') as file:
        raw_json = file.read()
    transactions = json.loads(raw_json)
    return transactions

