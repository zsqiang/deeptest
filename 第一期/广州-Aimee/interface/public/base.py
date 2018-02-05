#coding = utf-8
__author__ = 'Aimee'

from interface.public import Config

#对请求方式参数化
def get_host(EndPoint):
    host = Config.url()
    endpoint = EndPoint
    url = ''.join([host,endpoint])
    return url