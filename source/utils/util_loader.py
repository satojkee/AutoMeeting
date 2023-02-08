import json


def load_json(location: str) -> dict:
    """This function returns json-file data in python <dict> format.
    File location is required.

    :param location:    Setup file location in <str> format.
    """

    with open(location, 'r') as json_file:
        return json.load(json_file)


def update_json(location: str, new: dict) -> None:
    """This function updates json file with new data.
    * !WARNING! >> OVERRIDING procedure.

    :param location: json file location as string.
    :param new: new json data as dict.
    """

    current_data = load_json(location)
    current_data.update(new)
    with open(location, 'w') as json_file:
        json.dump(current_data, json_file)
        json_file.close()
