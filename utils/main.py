from loading_data import load_data
from validate_data import get_latest_transactions, get_latest_transaction_numbers, keep_executed
from output import output_transactions
import pathlib


def main():
    dir_path = pathlib.Path.cwd().parents[0]
    path = pathlib.Path(dir_path, 'source files', 'operations.json')
    transactions = load_data(path)
    validated_transactions = keep_executed(transactions)
    needed_transactions = get_latest_transactions(validated_transactions, get_latest_transaction_numbers(validated_transactions))
    output_transactions(needed_transactions)


if __name__ == "__main__":
    main()
