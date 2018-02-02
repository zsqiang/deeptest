# -*- coding: utf-8 -*-
__author__="大霞"

import json
#Json解析
#在Python中，提供了标准的json库来对json串进行解码和编码解析
"""
常用的函数如下
json.dumps
将python对象编码成json字符串, 返回json串
json.loads
将已编码的json串解码为python对象，返回python对应的数据类型
"""
"""
Python对象和JSON类型转化对照：
字典dict--Object
list列表、tuple元组--arry
str字符串--string
int、long、float--number
True--true
False--false
None--none
"""
if __name__=="__main__":
    #json串转换成dict（字典）实例
    print("将json转换成Python对象：")
    json_str='{"name":"开源优测","url":"www.testing.com","id":"DeepTest"}'
    #原类型
    print("原类型：",type(json_str))
    #转换为Python对象
    json_dict=json.loads(json_str)
    print("转换后类型",type(json_dict))

    #将dict（字典）转换成json串
    print("将字典转换成json串")
    json_dict={
        "name":"测试",
        "url":"www.testing.com",
        "id":"DeepTest"
    }
    print("类型：",type(json_dict))
    #将原类型转换成字符串类型
    print(json_dict)
    json_str=json.dumps(json_dict)

    print("转换后类型是：",type(json_str))
    print(json_str)
    print(json_str.encode('utf-8').decode('unicode_escape'))

    print("json串解析高级实例")
    json_demo = """
           {
               "weixin": [
                   {
                       "name": "开源优测",
                       "uid": "DeepTest",
                       "desc": "分享开源测试技术"
                   },
                   {
                       "name": "开源优测_demo",
                       "uid": "DeepTest_demo",
                       "desc": "分享开源测试技术_demo"
                   }
               ],
               "web": [
                   {
                       "url": "www.testingunion.com",
                       "name": "开源优测社区",
                       "desc": "分享各类开源测试技巧"
                   },
                   {
                       "url": "www.testingunion.com_demo",
                       "name": "开源优测社区_demo",
                       "desc": "分享各类开源测试技巧_demo"
                   }
               ]
           }
       """
    print("-"*30)
    #将json串转换成字典
    json_dict=json.loads(json_demo)
    #遍历字典
    for (k,v) in json_dict.items():
        # 输出第一层级，k为weixin、web；v为其对应的列表数据[]
        print(k,":",v)
        for data in v:
            #输出第二层级，遍历列表
            #v为{}
            for (data_k,data_v) in data.items():
                #输出第三层级，字典
                print(" ",data_k,":",data_v)