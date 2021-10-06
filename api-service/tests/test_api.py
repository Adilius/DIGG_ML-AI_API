# Integration test root URL of API service
from unittest import IsolatedAsyncioTestCase

import unittest
from unittest import mock
import json
import requests
from app.router import api

class test_root(IsolatedAsyncioTestCase):    
    async def test_root(test_app):
        response = await api.root()
        assert response == {
            "Success": "Hello World!"
        }
    
class test_url(IsolatedAsyncioTestCase):
    async def test_url(test_app):

        # Test valid request
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.text = '{"Hello":"World"}'
            mock_get.return_value.status_code = 200
            mock_get.return_value.ok = True
            mock_get.return_value.headers = {"content-type":"application/json"}
            valid_return = await api.url("http://valid.url")
            assert valid_return == {"Success": "URL valid"}

        # Test invalid URL request
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.text = '{"Hello":"World"}'
            mock_get.return_value.status_code = 200
            mock_get.return_value.ok = True
            mock_get.return_value.headers = {"content-type":"application/json"}
            invalid_url_return = await api.url("http://valirl")
            assert invalid_url_return == {"Error": "URL invalid"}

        # Test invalid status code request
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.text = '{"Hello":"World"}'
            mock_get.return_value.status_code = 404
            mock_get.return_value.ok = False
            mock_get.return_value.headers = {"content-type":"application/json"}
            invalid_status_code_return = await api.url("http://valid.url")
            assert invalid_status_code_return == {"Error": "Status code: 404"}

        # Test invalid content-type request
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.text = '{"Hello":"World"}'
            mock_get.return_value.status_code = 200
            mock_get.return_value.ok = True
            mock_get.return_value.headers = {"content-type":"hello world"}
            invalid_content_type_return = await api.url("http://valid.url")
            assert invalid_content_type_return == {'Error': 'Invalid content-type'}

        # Test invalid JSON parse request
        with mock.patch('requests.get') as mock_get:
            #TODO
            pass

        # Test invalid CSV parse request
        with mock.patch('requests.get') as mock_get:
            #TODO
            pass
 
class test_eval(IsolatedAsyncioTestCase):    
    async def test_eval(test_app):
        #TODO
        pass
        # Test invalid request
#        with mock.patch('data_handler.get_data') as mock_get:
#            valid_return = await api.eval("")
#            assert valid_return == {"Success": "URL valid"}
