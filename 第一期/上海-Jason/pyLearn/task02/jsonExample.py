# _*_ coding : utf-8 _*_
__author__ = "Jason"

'''
概述
    JSON是JavaScript Object Notation的简称，是一种轻量级的数据交换格式，易于阅读和编写，
    是目前前后端最常用的数据交换格式之一。
标准库
    在Python中，提供了标准的JSON库来对JSON串进行解码和编码解析。
    
    常用的函数如下：
    json.dumps          将JSON对象编码成JSON字符串，返回JSON串
    json.loads          将已编码的JSON串解码为Python对象，返回Python对应的数据类型
    
    下面来看Python对象和JSON类型的转化对照表
    Python类型                        JSON
    字典dict                          object
    list列表、tuple元组               array
    str字符串                         string
    int、long、float                  number
    True                              true
    False                             false
    None                              null
'''
import json

if __name__ == "__main__":
    print("字典转JSON串")

    json_dict = {
        "name":"开源优测",
        "url":"www.testingunion.com",
        "id":"DeepTest"
    }
    print("原类型：",type(json_dict))#原类型： <class 'dict'>

    #将字典转换成JSON串
    #会被转换为字符串类型
    json_str = json.dumps(json_dict)
    print(json_str)
    #{"name": "\u5f00\u6e90\u4f18\u6d4b", "url": "www.testingunion.com", "id": "DeepTest"}
    #此处需转码
    print(type(json_str))#<class 'str'>
    print('-'*50)

    #json_str1 = json.dumps(json_dict,encoding="utf-8",ensure_ascii=False)
    #json_str2 = json.dumps(json_dict,encoding="utf-8")
    json_str3 = json.dumps(json_dict,ensure_ascii=False)
    print(type(json_str3),json_str3)
    #<class 'str'> {"name": "开源优测", "url": "www.testingunion.com", "id": "DeepTest"}
