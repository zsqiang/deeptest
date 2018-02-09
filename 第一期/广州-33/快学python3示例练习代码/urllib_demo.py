# coding = utf-8
# urllib基本功能示例

import urllib.request

if __name__ == "__main__":
    print("urllib基本示例")

    url = "http://www.baidu.com"

    # 访问下百度
    response = urllib.request.urlopen(url)

    # 打印状态码
    print(response.status)

    # 打印状态码对应的可读性文字说明，例如在http协议里，200对应OK
    print(response.reason)

    # 打印请求返回的header
    print(response.headers)

    # 打印请求返回的数据
    print(response.read().decode("utf-8"))