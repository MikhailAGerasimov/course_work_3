import datetime
def keep_exceuted(transactions):
    '''
    Оставляет в списке, только транзакции со статусом 'EXECUTED'
    :param transactions: исходный список транзакций
    :return: список транзакций только со статусом 'EXECUTED'
    '''
    return [sub for sub in transactions if 'EXECUTED' in list(sub.values())]


def get_latest_transaction_numbers(transactions):
    '''
    Функция возвращаюшая список номеров последних 5 транзакций
    :param transactions: список словарей всех тразакций
    :return: список номеров последних 5 тразакций
    '''
    dates = []
    num = 5
    i=0
    for sub in transactions:
        date = sub.get('date')
        date = date.replace('T',' ')
        list = [datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S.%f'), i]
        dates.append(list)
        i+=1
    dates.sort(key=lambda x: x[0],reverse= True)
    return [elem[1] for elem in dates[0:num]]


def get_latest_transactions(transactions, numbers):
    '''
    Функция возвращает последние n транзакций
    :param transactions: список всех транзакций
    :param numbers: список номеров последних n транакций
    :return: список последних n транзакций
    '''
    return [transactions[numbers[i]] for i in range(len(numbers))]