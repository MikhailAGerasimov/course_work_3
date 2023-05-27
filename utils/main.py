import loading_data, validate_data
import pathlib
from pathlib import Path

dir_path = pathlib.Path.cwd().parents[0]
path = Path(dir_path, 'source files', 'operations.json')
transactions = loading_data.load_data(path)
validated_transactions = validate_data.keep_exceuted(transactions)







for sub in validated_transactions:
    print(sub)