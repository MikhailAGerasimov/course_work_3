import json
import pathlib
from pathlib import Path

def load_data(path):
    with open(path, encoding='utf-8') as file:
        raw_json = file.read()
    transactions = json.loads(raw_json)
    return transactions

# dir_path = pathlib.Path.cwd().parents[0]
# path = Path(dir_path, 'source files', 'operations.json')
# print(load_data(path))