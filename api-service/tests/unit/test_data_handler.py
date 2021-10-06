# Test data_handler of API service

import unittest
from unittest import mock
import json

import requests
from requests.models import Response
from app.dependencies import data_handler

def test_validate_url(test_app):

    valid_response = data_handler.validate_url(url="http://broken.com")
    invalid_response = data_handler.validate_url(url="htp://broken.url")
    assert valid_response == {
        'Success':'URL valid'
    }
    assert invalid_response == {
        'Error':'URL invalid'
    }

# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, status_code, ok):
            self.status_code = status_code
            self.ok = ok

    if args[0] == '200':
        return MockResponse(200, True)
    elif args[0] == '404':
        return MockResponse(404, False)

@mock.patch('requests.get', side_effect=mocked_requests_get)
def test_request_url(test_app):
    success_status, _ = data_handler.request_url('200')
    error_status, _ = data_handler.request_url('404')
    assert success_status == {
        'Success': 'Status code: 200'
    }
    assert error_status == {
        'Error': 'Status code: 404'
    }

def test_validate_response(test_app):

    # Test json content-type
    r_json = requests.Response()
    r_json.headers['content-type'] = 'application/json'
    response = data_handler.validate_response(r_json)
    assert response == {
        'Success': 'Content-type: application/json'
    }

    # Test csv content-type
    r_csv = requests.Response()
    r_csv.headers['content-type'] = 'text/csv'
    response = data_handler.validate_response(r_csv)
    assert response == {
        'Success': 'Content-type: text/csv'
    }

    # Test invalid content-type
    r_invalid = requests.Response()
    r_invalid.headers['content-type'] = 'invalid'
    response = data_handler.validate_response(r_invalid)
    assert response == {
        'Error': 'Invalid content-type'
    }

def test_parse_json(test_app):

    # Invalid JSON data
    r_invalid = requests.Response()
    r_invalid._content = b'invalid'
    response = data_handler.parse_json(r_invalid)
    assert response == {
        'Error': 'Content can not be parsed to JSON'
    }

    # Valid JSON data
    r_valid = requests.Response()
    r_valid._content = b'{ "hello" : "world" }'
    response = data_handler.parse_json(r_valid)
    assert response == {
         "hello" : "world" 
    }

def test_parse_csv(test_app):

    # Invalid CSV data
    r_invalid = requests.Response()
    r_invalid._content = b'invalid'
    response = data_handler.parse_csv(r_invalid)
    assert response == {
        'Error': 'Content can not be parsed to JSON from CSV'
    }

    # Valid CSV data
    r_valid = requests.Response()
    r_valid._content = b'1,2,3\n1,2,3'
    response = data_handler.parse_csv(r_valid)
    assert response == {
        'results': [
            {
            '1':'1',
            '2':'2',
            '3':'3'
        }
        ]
    }