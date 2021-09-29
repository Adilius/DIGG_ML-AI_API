import requests
import json
import ast

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

# Get all results
def get_all_results():

    headers = {
        'accept': 'application/json'
    }

    response = requests.get('http://db_service:8003/get_all_data/', headers=headers)

    return response.text

# Get result using url and checksum
def get_result(url: str, checksum: str):

    headers = {
        'accept': 'application/json'
    }

    payload = {
        "url": url,
        "checksum" : checksum
    }

    response = requests.get(f'http://db_service:8003/get_data/', headers=headers, params=payload)
    response_dict = ast.literal_eval(response.text)
    evaluation_dict =  ast.literal_eval(response_dict['evaluation'])
    
    return evaluation_dict