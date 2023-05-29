from loading_data import load_data
from validate_data import get_latest_transactions, get_latest_transaction_numbers, keep_executed
from output import output_transactions



def main():

    # формирование списка выполненных транзакций
    validated_transactions = keep_executed(load_data('operations.json'))
    # формирование списка 5 последних транзакций
    needed_transactions = get_latest_transactions(validated_transactions, get_latest_transaction_numbers(validated_transactions))
    # вывод последних 5 транзакций
    output_transactions(needed_transactions)


if __name__ == "__main__":
    main()
