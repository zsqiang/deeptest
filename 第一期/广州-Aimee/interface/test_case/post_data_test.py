#coding:utf-8
__author__ = 'Aimee'

import unittest
import requests
import json
from interface.public import base
from interface.public import HttpService

class PostDateTest(unittest.TestCase):
    def setUp(self):
        endpoint = 'post'
        self.url = base.get_host(endpoint)
    def test_post_data_1(self):
        params = {'show_env': 1}
        data = {'a': 'aimee', 'b': '学测试'}
        #发送请求
        # r = requests.post(self.url,params=params,data=data)
        DataALL = {'params':params,' data': data}
        r = HttpService.MyHTTP(self.url).post(self.url,**DataALL)
        # resp = r.json()
        form = r['form']['a']
        self.assertEqual(form,'aimee')

    def tearDown(self):
        pass

if __name__ == "__main__":
        unittest.main()

