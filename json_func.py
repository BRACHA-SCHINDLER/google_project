import json
from os import close


def write_to_json(path,data):
    with open(path, "w") as the_file:
        json.dump(data, the_file)


def read_from_json(path):
    the_file = open(path)
    data = json.load(the_file)
    the_file.close()
    return data



