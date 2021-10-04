import unittest
from unittest import mock
import json

import requests
from requests.models import Response
from app.dependencies import database_handler

def test_get_result(test_app):

    # Check no return
    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.text = 'no_return'
        no_return = database_handler.get_result('no_return','no_return')

    assert no_return == {
        'Error':'Could not read result from database'
        }

    # Check wrong return
    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.text = '{"evaluation":"Hello World"}'
        wrong_return = database_handler.get_result('wrong_return','wrong_return')

    assert wrong_return == {
        'Error':'No such result in database'
        }

    # Check valid return
    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.text = '{"evaluation":\'{"Hello" : "World"}\'}'
        valid_return = database_handler.get_result('valid_return','')

    assert valid_return == {
        "Hello": "World"
    }

    


def test_store_result(test_app):
    pass

def test_get_all_results(test_app):
    pass