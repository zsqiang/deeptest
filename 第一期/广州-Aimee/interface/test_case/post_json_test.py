#coding:utf-8
__author__ = 'Aimee'
import unittest
import requests
import json
from interface.public import base

class PostJsonTest(unittest.TestCase):
    def setUp(self):
        endpoint = 'post'
        self.url = base.get_host(endpoint)
    def test_post_json(self):
        data = {
            "employees": [
                {"firstName": "Bill", "lastName": "Gates"},
                {"firstName": "George", "lastName": "Bush"},
                {"firstName": "Thomas", "lastName": "Carter"}
            ]
        }
        r = requests.post(self.url,json=data)
        resp = json.loads(r.text)
        employees = resp.get('data')
        self.assertIsInstance(employees,str)

    def tearDown(self):
        pass

    if __name__ =="__main__":
        unittest.main()


