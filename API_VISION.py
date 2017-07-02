import json

import requests


class Response:
    def __init__(self, status_code, content, celebrities):
        self.status_code = status_code
        self.content = content
        self.celebrities = celebrities


def detect_celebrity(thing, api_key, timeout=None):
    if type(thing) is str:
        with open(thing, 'rb') as fp:
            blob = fp.read()
    elif type(thing) is bytes:
        blob = thing
    else:
        raise TypeError("Cannot recognise image argument. "
                        "Expected filename string or bytes data.")
    return _detect_celebrity(blob, api_key, timeout)


def _detect_celebrity(binary_blob, api_key, timeout):
    params = {
        'visualFeatures': "description",
        'details': 'Celebrities',
        'language': 'en',
    }
    headers = {
        'Ocp-Apim-Subscription-Key': api_key,
        'Content-Type': 'application/octet-stream'
    }
    url = 'https://westus.api.cognitive.microsoft.com/vision/v1.0/analyze'

    r = requests.request('post', url, data=binary_blob,
                         headers=headers,
                         params=params, timeout=timeout)

    json_r = json.loads(r.content.decode('utf-8'))
    # print(json_r)
    # print(r)
    response = Response(r.status_code, json_r, json_r.get('categories', {}))
    return response
