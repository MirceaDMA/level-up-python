import json

def save_dict(dict_to_save, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(dict_to_save))

def open_dict(file_path):
    with open(file_path, encoding="utf-8") as f:
        new_dictionary = json.loads(f.read())
    return new_dictionary
