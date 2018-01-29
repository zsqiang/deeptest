# _*_ coding : utf-8 _*_
__author__ = "Jason"

import urllib.request

if __name__ == "__main__":
    print("urllib基本实例")

    url = "http://www.baidu.com"

    # 访问下百度
    response = urllib.request.urlopen(url)

    # 打印下状态码
    print(response.status)# 200

    # 打印下状态码对应的可读性文字说明，例如在http协议里，200 对应 OK
    print(response.reason)# OK

    # 打印下请求返回的header
    # 返回相应头
    print(response.headers)

    # 打印下请求返回的数据
    # 返回整个页面的html
    print(response.read().decode("utf-8"))