import validators
import requests
import json
import csv

def validateURL(url: str):
    if validators.url(url):
    #if True:
        validated_response = getURL(url)
        return validated_response
    else:
        return {'Error':'URL invalid'}

def getURL(url: str):

    # Try to get resource from url 
    response = requests.get(url)

    # Check if we got succesful response
    if not response.ok:
        return {'Error': f'Status code: {response.status_code}'}
    else:
        validated_response = validateResponse(response)
        return(validated_response)


def validateResponse(response):

    # Get JSON
    if 'application/json' in response.headers.get('content-type'):
        return parseJSON(response)

    # Get JSON from CSV
    if 'text/csv' in response.headers.get('content-type'):
        return parseCSV(response)

    # Any other content type    
    try:
        content_type = response.headers.get('content-type')
        return {'Error': f'Wrong content-type: {content_type}'}
    except:
        return {'Error': 'Wrong content-type'}

def parseJSON(response):
    try:
        response_json = response.json()
    except:
        return {'Error': 'Content can not be parsed to JSON'}
    return response_json

def parseCSV(response):
    try:
        # Decode 
        decoded_content = response.content.decode('utf-8')

        # Get delimiter
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(decoded_content)
        
        # Read CSV content
        csv_reader = csv.reader(decoded_content.splitlines(), delimiter=dialect.delimiter)

        # Get column names
        fields = list(next(csv_reader))
        json_list = []
        
        # Create list of dicts
        for row in csv_reader:
            dict_row = {}
            for index, col in enumerate(row):
                key_value = {fields[index]:col}
                dict_row.update(key_value)
            json_list.append(dict_row)

        # Create dict that we return
        json_dict = {}
        json_dict['data'] = json_list
        return json_dict

    except:
        return {'Error': 'Content can not be parsed to JSON from CSV'}
