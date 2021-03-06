import unittest
from unittest import mock
import json

import requests
from requests.models import Response
from app.dependencies import database_handler

def test_get_result(test_app):

    # Check no data return
    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.text = 'Error'
        no_return = database_handler.get_result('no_return')

    assert no_return == {
        'Error':'No data in database'
        }

    # Check wrong response return
    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.text = '{"evaluation":Hello World}'
        wrong_return = database_handler.get_result('wrong_return')

    assert wrong_return == {
         'Error':'Could not read result from database'
        }

    # Check wrong response return
    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.text = '{"evaluation":\'{"Hello" : World}\'}'
        wrong_return = database_handler.get_result('wrong_return')

    assert wrong_return == {
         'Error':'Could not read evaluation from result'
        }

    # Check valid return
    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.text = '{"evaluation":\'{"Hello" : "World"}\'}'
        valid_return = database_handler.get_result('valid_return')

    assert valid_return == {
        "Hello": "World"
    }


def test_store_result(test_app):
    with mock.patch('requests.post') as mock_get:
        mock_get.return_value.text = 'test'
        test = database_handler.store_result('test','test')
        assert test == 'test'


def test_get_all_results(test_app):
    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.text = 'test'
        test = database_handler.get_all_results()
        assert test == 'test'