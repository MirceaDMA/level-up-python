import json

def save_dict(dict_to_save, file_path):
    with open(file_path, "wb", encoding="utf-8") as file:
        file.write(json.dumps(dict_to_save))

def open_dict(file_path):
    with open(file_path, "rb") as file:
        return json.loads(file.read())

# PICKLE
# import pickle

# def save_dict(dict_to_save, file_path):
#     with open(file_path, "wb") as file:
#         pickle.dump(dict_to_save, file)

# def load_dict(file_path):
#     with open(file_path, "rb") as file:
#         return pickle.load(file)