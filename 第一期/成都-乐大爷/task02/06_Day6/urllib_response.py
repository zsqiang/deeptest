# -*- coding:utf-8 -*-

__author__ = 'catleer'

import urllib.request

if __name__ == "__main__":
    print("urllib基本实例")
    url = "http://www.baidu.com"

    # 访问下百度
    response = urllib.request.urlopen(url)

    # 打印状态码
    print(response.status)

    # 打印状态码对应的可读性文字说明
    print(response.reason)

    # 打印下请求返回的headers
    print(response.headers)

    # 打印下请求返回的数据
    # print(response.read().decode("utf-8"))