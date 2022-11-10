import json


def retrieveJsonData(path: str):
    file = open(path, "r")
    json_data = json.load(file)
    file.close
    return json_data
