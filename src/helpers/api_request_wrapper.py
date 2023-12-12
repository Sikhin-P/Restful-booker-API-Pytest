# HTTP Request Generic Functions
import json
import requests


def get_request(url, auth, in_json):
    response = requests.get(url=url, auth=auth)
    if in_json is True:
        return response.json()
    return response


def post_request(url, auth, headers, payload, in_json):
    response = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response


def put_request(url, auth, headers, payload, in_json):
    response = requests.put(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response


def patch_request(url, auth, headers, payload, in_json):
    response = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return response.json()
    return response


def delete_request(url, auth, headers, in_json):
    response = requests.delete(url=url, auth=auth, headers=headers)
    if in_json is True:
        return response.json()
    return response
