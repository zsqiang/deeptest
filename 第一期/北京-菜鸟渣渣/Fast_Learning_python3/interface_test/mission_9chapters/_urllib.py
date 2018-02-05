#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")
'''
在python3中urllib由以下几个模块构成：

parse
request
response
robotparser
error
下面对这个几个模块进行一一分享。
'''


'''
parse模块

parse模块定义了统一的接口并实现了URL解析和引用功能。

'''
import urllib.request
from urllib.parse import urlparse
import  urllib.response
from http.client import HTTPResponse


if __name__ == '__main__':

    url='//www.cwi.nl:80/%7Eguido/Python.html'
    result=urlparse(url)

    print(result)

    print("协议: ", result.scheme)
    print("连接字符串：", result.netloc)
    print("网络位置部分:",result.query)
    print("端口号：", result.port)
    print("uri资源：", result.path)
    print("用户名：", result.username)
    print("密码：", result.password)
    print("fragment:",result.fragment)

    '''
    requset模块
    
    这个模块可以说是urllib最核心的模块了，其定义了系列函数、类用于实现http/https相关协议功能。
    
    '''

    respons=urllib.request.urlopen("https://www.baidu.com")
    print(respons.info())
    print(respons.geturl())
    print(respons.getcode())
    print(respons.read())

    '''
    response模块

    response模块比较简单，其定义了http response基本出来方法，作为基类存在，大家有兴趣的可以研究下其源码，了解去编码风格及实现，有利于深入掌握如何处理http的返回值。
    
    这里不做实例演示，因为其提供的方法、功能主要在request模块中进行了应用。
    
    '''

    '''
    robotparser模块

robotparser模块提供了一个单独的类：robotfileparser，用于处理robot.txt文件。

至于这个文件是干嘛用的你可以访问：http://www.robotstxt.org/norobots-rfc.txt 进行了解、学习。

当你需要研究爬虫时，这个robots.txt是必须深入研究的东西。
    
    '''

    '''
    error模块

error模块定义了url、http相关的错误基类，总共不到100行代码，很简洁，这里就不做说明了。
    
    '''