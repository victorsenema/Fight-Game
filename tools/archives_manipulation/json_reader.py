import json

def get_json_data(json_path):
    with open(json_path, encoding="utf-8") as f:
        return json.load(f)
    return None