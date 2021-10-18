import unittest
from unittest import mock
import json
import requests
from app.router import api

def test_root_ui(test_app):
    response = test_app.get('/')
    assert response.status_code == 200
    assert response.headers.get('content-type') == "application/json"
    assert response.json() == {
        "Success": "Hello World!"
    }