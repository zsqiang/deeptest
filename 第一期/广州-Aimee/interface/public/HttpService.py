#coding = utf-8
__author__ = 'Aimee'

import requests
import json
#类的封装
class MyHTTP():
    def __init__(self,url):
        self.url = url
    #写死了参数个数
    # def get(self,url,params,headers):
    #     resp = requests.get(url,params=params,headers=headers)
    #     text = resp.json()
    #     return text

    #   参数参数化
    def get(self,url,**DataALL):
        params = DataALL.get('params')
        headers = DataALL.get('headers')
        resp = requests.get(url,params=params,headers=headers)
        text = resp.json()
        return text

    def post(self,url,**DataALL):
        params = DataALL.get('params')
        headers = DataALL.get('headers')
        data = DataALL.get('data')
        json = DataALL.get('json')
        resp = requests.get(url,params=params,headers=headers,data=data,json=json)
        text = resp.json()
        return text






