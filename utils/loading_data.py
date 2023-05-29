import json
import pathlib


def load_data(file_name):
    """
    Фнукция получает на вход путь до файла с транзакциями
    и возвращает список словарей
    :param path: путь до файла
    :return: список словарей с транзакциями
    """
    path = pathlib.Path(__file__).parent.parent / 'source files' / file_name
    with open(path, encoding='utf-8') as file:
        raw_json = file.read()
    transactions = json.loads(raw_json)
    return transactions
