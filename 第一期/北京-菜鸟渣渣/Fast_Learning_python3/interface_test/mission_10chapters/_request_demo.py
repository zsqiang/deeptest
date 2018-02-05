#coding=utf-8

import logging

import requests
# import requests.Response

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")


'''
继续requests基础分享，本文主要分享以下内容：

请求头定制

POST请求
'''


if __name__ != '__main__':
    print("开源优测 - requests自定义请求头基本示例")

    url = "http://www.baidu.com"

    headers={ "user-agent": "www.testingunion.com","custom-head":"DeepTest"}

    r=requests.get(url,headers=headers)
    print(r.text)



'''
注：所有的header值必须是string、bytestring或unicode，虽然传递unicode header是允许的，但不建议这样做

python requests_headers_demo.py
在运行上述命令前，先启动wireshark，用来抓取报文，看下我们自定义的headers是否正常被设置。
'''

if __name__ != '__main__':
    print("requests post示例")

    # 目标url
    url = "http://httpbin.org/post"

    # 请求头headers
    headers = {"custom-header": "mypost"}

    # 要post的数据
    data = {"data_1": "deeptest", "data_2": "testingunion.com"}

    # 发送post请求
    r = requests.post(url, data=data, headers=headers)

    # 输出结果
    # print(r.text)

    #postjson数据到服务。
if __name__ == '__main__':

    print("requests post json数据示例")

    # 目标服务url
    url = "http://jsonplaceholder.typicode.com/posts"

    # 自定义头
    headers = {
        "custom-post": "my-post",
        "custom-header": "my-json-header"
    }

    # 要post的数据
    json_data = {
        "title": "deeptest",
        "body": "开源优测",
        "userId": "1"
    }
    print(type(json_data))

    # post json格式的数据
    r = requests.post(url, json=json_data, headers=headers)

    # 打印下返回结果
    print(r.text)