#coding:utf-8
__author__ = 'Aimee'
import json
import requests
import unittest
from interface.public import base  #加入绝对路径
from interface.public import HttpService

class GetParamsHeadersTest(unittest.TestCase):
    #get有params和headers测试
    def setUp(self):
        endpoint = 'get'
        self.url = base.get_host(endpoint)
        #提取公共部分
    def test_params_headers(self):
        params = {'show_env': 1}
        headers ={'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate', 'User-Agent': 'python-requests/2.18.4', 'Accept': '*/*'}
        #发送请求
        DataALL = {'params':params,' headers': headers}
        resp = HttpService.MyHTTP(self.url).get(self.url,**DataALL)
        # r = requests.get(self.url,params=params,headers=headers)
        # resp = r.json()
        User_Agent = resp['headers']['User-Agent']
        self.assertEqual(User_Agent,'python-requests/2.18.4')
        self.assertIn('python',User_Agent)

    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()