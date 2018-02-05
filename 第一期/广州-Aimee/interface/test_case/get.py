#coding = utf -8

__author__ = 'Aimee'


import requests
import json

host = 'https://httpbin.org/'
endpoint = 'get'
url = ''.join([host,endpoint])
params = {'show_env' :1}

#给服务器发送请求
# r = requests.get(url) #无参数
r = requests.get(url,params=params)  #有参数
r = requests.get(url,params=params,headers =None)  #有headers

print(r.url) #获取url
print(r.status_code,r.reason,r.headers) #获取状态码

print(r.text) #文本形式 Unicode文本形式
# print(type(r.text))
# print(r.content)  #byte形式,支持图片 文件
# print(type(r.content))

# print(r.headers) #响应头
# print(r.request.headers)  #请求头
# print(r.request.url)
# print(r.request.method)

#常用字典形式
# res = r.json()
# print(type(res))
# print(res)
# #获取响应数据
# print(res['headers']['Connection'])

#字符串只能通过切片方式获取数据 eval函数
# print(eval(r.text)['headers'])




