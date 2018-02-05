#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

'''
从本文开始分享requests相关知识，及如何用requests进行接口测试。

requests号称：是唯一的一个非转基因的Python HTTP库，人类可以安全享用。

'''


'''
下面我们看看requests的功能特色：

Keep-Alive & 连接池
国际化域名和URL
带持久化Cookie的会话
浏览器式的SSL认证
内容自动解码
basic/Digest认证
key/value Cookie管理
自动解压
Unicode响应
HTTP/HTTPS代理支持
文件分块上传
流下载
连接超时
分块请求
支持.netrc
'''

import  requests

if __name__ == '__main__':
    r=requests.get('https://api.github.com')

    status_code=r.status_code

    headers=r.headers

    content_type=r.headers['Content-type']

    code=r.encoding

    json_data=r.json()

    print("状态码： ", status_code)
    print("返回头： ", headers)
    print("content-type： ", content_type)
    print("编码：", code)
    print("文本内容： ", type(r.text),r.text)
    print("json串内容: ", type(json_data),json_data)


