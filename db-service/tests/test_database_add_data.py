import requests_mock
import unittest
import requests
import json

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = "string"
        cls.checksum = "string"
        cls.evaluation = "string"

    def test_store_result_success(self):
        headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        }

        return_value = {
            'url': self.url,
            'checksum': self.checksum,
            'evaluation': self.evaluation
        }

        test_response_payload = {
            'url': self.url,
            'checksum': self.checksum,
            'evaluation': self.evaluation
        }

        with requests_mock.Mocker() as rm:
            rm.post(
                'http://db_service:8003/add_data/', 
                json=return_value, 
                status_code=201)
            response = requests.post(
                'http://db_service:8003/add_data/',
                headers=headers, 
                data=return_value)

            data_json = json.dumps(test_response_payload)

            assert response.status_code == 201
            self.assertEqual(
                response.text, 
                data_json, 
                'Failed to post result to database')
        