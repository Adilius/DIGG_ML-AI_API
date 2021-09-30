# Test data_handler of API service

import unittest
from unittest import mock

import requests
from app.dependencies import data_handler

def test_validate_url(test_app):

    response = data_handler.validateURL(url="htp://broken.url")
    assert response == {
        "Error": "URL invalid"
    }

# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, status_code, ok):
            self.status_code = status_code
            self.ok = ok

    return MockResponse(404, None)

@mock.patch('requests.get', side_effect=mocked_requests_get)
def test_get_url(test_app):
    response = data_handler.getURL('')
    assert response == {
        'Error': 'Status code: 404'
    }

def test_validate_response(test_app):
    r = requests.Response()
    r.headers['content-type'] = 'err'
    response = data_handler.validateResponse(r)
    assert response == {
        'Error': 'Wrong content-type: err'
    }