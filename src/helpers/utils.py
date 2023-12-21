# Common utility functions

def common_headers_json():
    headers = {"Content-Type": "application/json"}
    return headers


def common_headers_xml():
    headers = {"Content-Type": "application/xml"}
    return headers


# Functions to read from CSV, Excel, yaml, text, json, etc.

def load_from_json(file_path):
    import json
    file = open(file_path)
    data = json.load(file)
    file.close()
    return data
