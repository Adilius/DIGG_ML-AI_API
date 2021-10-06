import requests
import json
import ast

# Headers sent with HTTP request to database
headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

# Store result in database
def store_result(url: str, checksum: str, evaluation: dict):

    eval_json = json.dumps(evaluation)

    # Collect data to send
    data = {
        'url' : url,
        'checksum': checksum,
        'evaluation' : eval_json
    }

    # Convert data to JSON
    data_json = json.dumps(data)

    response = requests.post(
        'http://db_service:8003/add_data/',
        headers=headers, 
        data=data_json)

    return response.text

# Get result using url and checksum
def get_result(url: str, checksum: str):


    payload = {
        "url": url,
        "checksum" : checksum
    }

    response = requests.get(
        'http://db_service:8003/get_data/',
        headers=headers, 
        params=payload)

    print(f'response')
    print(response.text)
    print(type(response.text))

    # Convert response to dictionary
    try:
        response_dict = ast.literal_eval(response.text)
    except:
        return {
            'Error':'Could not read result from database'
        }

    # Extract evaluation from response
    try:
        evaluation_dict =  ast.literal_eval(response_dict['evaluation'])
    except:
        return {
            'Error':'Could not read evaluation from result'
        }

    
    return evaluation_dict

# Get all results
def get_all_results():

    response = requests.get(
        'http://db_service:8003/get_all_data/', 
        headers=headers)

    return response.text
