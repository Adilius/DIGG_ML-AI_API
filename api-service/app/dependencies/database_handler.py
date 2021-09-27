import requests
import json

# Store result in database
def store_result(url: str, checksum: str, evaluation: dict):

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    eval_json = json.dumps(evaluation)

    data = {
        'url' : url,
        'checksum': checksum,
        'evaluation' : eval_json
    }

    data_json = json.dumps(data)
    #print(data_json)

    response = requests.post('http://db_service:8003/add_data/', headers=headers, data=data_json)
    print(response.text)

    return response.text

# Get result using url and checksum
def get_result():

    headers = {
        'accept': 'application/json'
    }

    response = requests.get('http://db_service:8003/get_data/', headers=headers)

    return response.text