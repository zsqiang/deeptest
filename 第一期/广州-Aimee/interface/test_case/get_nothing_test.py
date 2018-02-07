#coding:utf-8

import requests
import unittest
import json
from interface.public import base
from interface.public import HttpService

class GetNothingTest(unittest.TestCase):
    def setUp(self):
        endpoint = 'get'
        self.url = base.get_host(endpoint)
        params = {'show_env': 1}
    def test_1(self):
        # 校验返回status_code是否为200
        #发送请求
        # r = requests.get(self.url)
        r = HttpService.MyHTTP(self.url).get(self.url)
        res = str(r)
        status_code = res.status_code
        self.assertEqual(status_code, 200)

    def test_2(self):
        res = HttpService.MyHTTP(self.url).get(self.url)
        # res = r.json()
        connect = res['headers']['Connection']
        self.assertEqual(connect, 'close')

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()



# 给服务器发送请求
# r = requests.get(url) #无参数
# r = requests.get(url,params=params)  #有参数
# r = requests.get(url,params=params,headers =None)  #有headers
#
# print(r.url) #获取url
# print(r.status_code,r.reason,r.headers) #获取状态码
#
# print(r.text) #文本形式 Unicode文本形式
# print(type(r.text))
# print(r.content)  #byte形式,支持图片 文件
# print(type(r.content))

# print(r.headers) #响应头
# print(r.request.headers)  #请求头
# print(r.request.url)
# print(r.request.method)

# 常用字典形式
# res = r.json()
# print(type(res))
# print(res)
# #获取响应数据
# print(res['headers']['Connection'])

# 字符串只能通过切片方式获取数据 eval函数
# print(eval(r.text)['headers'])
