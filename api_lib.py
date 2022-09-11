import requests
import os
import json


def call_ugig_api(body):

    headers = {
        'x-api-key': os.environ['UGIG_ADMIN_API_KEY'],
        'admin_key': os.environ['ADMIN_KEY'],
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", os.environ['API_ENDPOINT'], headers=headers, data=body)
    return json.loads(response.text)

