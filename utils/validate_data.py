def keep_exceuted(transactions):
    '''
    Оставляет в списке, только транзакции со статусом 'EXECUTED'
    :param transactions: исходный список транзакций
    :return: список транзакций только со статусом 'EXECUTED'
    '''
    return [sub for sub in transactions if 'EXECUTED' in list(sub.values())]