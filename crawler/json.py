import json
import os

def save_json_to_file(file_path, data):
    if not data:
        if os.path.isfile(file_path):
            os.remove(file_path)
        return

    with open(file_path, 'w+') as f:
        json.dump(data, f)
        print('\n\tArquivo salvo.')

def load_json_from_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            print('\tArquivo existente carregado na memória.\n')
            return json.load(f)
    
    return []
