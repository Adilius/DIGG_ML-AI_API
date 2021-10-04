import validators
import requests
import json
import csv

# Call this from api
def get_data(url:str):

    validated_url = validate_url(url)

    #If we got error
    if next(iter(validated_url)) == 'Error':
        return validated_url

    status, response = request_url(url)

    #If we got error
    if next(iter(status)) == 'Error':
        return status

    validated_response = validate_response(response)

    #If we got error
    if next(iter(validated_response)) == 'Error':
        return validated_response

    #If we got JSON
    if 'Content-type: application/json' in validated_response.values():
        parse_response = parse_json(response)
        return parse_response

    #If we got CSV
    if 'Content-type: text/csv' in validated_response.values():
        parse_response = parse_csv(response)
        return parse_response
    
    return {
            "Error": "URL could not be validated"
        }


# Check if URL is valid
def validate_url(url: str):
    if validators.url(url):
        return {'Success':'URL valid'}
    else:
        return {'Error':'URL invalid'}

# Make HTTP GET request to URL
def request_url(url: str):

    # Try to get resource from url
    try:
        response = requests.get(url)
    except:
        return (
            { 'Error':'Failed to send request to url'},
            None)

    # Check if we got succesful response
    if response.ok:
        return (
            {'Success': f'Status code: {response.status_code}'},
            response)
    else:
        return (
            {'Error': f'Status code: {response.status_code}'},
            None)

# Validates our response
def validate_response(response):

    content_type = response.headers.get('content-type')

    # Get JSON
    if 'application/json' in content_type:
        return {'Success': 'Content-type: application/json'}

    # Get JSON from CSV
    if 'text/csv' in response.headers.get('content-type'):
        return {'Success': 'Content-type: text/csv'}
        

    # Any other content type    
    return {'Error': 'Invalid content-type'}

# Parse response from JSON
def parse_json(response):
    try:
        response_json = response.json()
    except:
        return {'Error': 'Content can not be parsed to JSON'}
    return response_json

# Parse response from CSV
def parse_csv(response):
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

        # If no data was captured, then parsing failed
        if len(json_list) == 0:
            return {'Error': 'Content can not be parsed to JSON from CSV'}

        # Create dict that we return
        json_dict = {}
        json_dict['results'] = json_list
        return json_dict

    # If parsing failed for some unforseen error
    except:
        return {'Error': 'Content can not be parsed to JSON from CSV'}
