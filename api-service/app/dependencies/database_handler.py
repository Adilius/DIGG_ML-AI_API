import requests
import json
import ast

# Headers sent with HTTP request to database
headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

# Store result in database
def store_result(url: str, evaluation: dict):

    eval_json = json.dumps(evaluation)

    # Collect data to send
    data = {
        'url' : url,
        'evaluation' : eval_json
    }

    # Convert data to JSON
    data_json = json.dumps(data)

    response = requests.post(
        'http://db_service:8003/add_data/',
        headers=headers, 
        data=data_json)

    return response.text

# Get result using url
def get_result(url: str):


    payload = {
        "url": url
    }

    try:
        response = requests.get(
            'http://db_service:8003/get_data/',
            headers=headers, 
            params=payload)
    except:
        return {
            'Error':'Failed to get from database'
        }

    #print(f'Database response: {response.text}')

    if any(substr in response.text for substr in ['Error','error']):
        return {
            'Error':'No data in database'
        }

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
