import requests_mock
import unittest
import json

from app.dependencies.database_handler import store_result

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = "string"
        cls.checksum = "string"
        cls.evaluation = "string"

    def test_store_result_success(self):
        
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
            response = store_result(
                self.url, self.checksum, self.evaluation
            )

            data_json = json.dumps(test_response_payload)

            self.assertEqual(
                response, 
                data_json, 
                'Failed to post result to database')
        