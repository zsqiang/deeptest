# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
json.dumps
将python对象编码成json字符串, 返回json串

json.loads
将已编码的json串解码为python对象，返回python对应的数据类型
"""

import json

def json_to_dict():
    print("json转dict")

    json_str = '{"name": "开源优测", "url": "www.testingunion.com", "id": "DeepTest"}'
    print("原类型：", type(json_str))

    json_dict = json.loads(json_str)
    print("转换后的类型：", type(json_dict))

    # 遍历字典
    for (k, v) in json_dict.items():
        print(k, " ： ", v)

def dict_to_json():
    print("dict转json")

    json_dict = {"name": "开源优测", "url": "www.testingunion.com", "id": "DeepTest"}
    json_str = json.dumps(json_dict)

    print(json_str)


# json_to_dict()
# dict_to_json()

# 实例

if __name__ == "__main__":
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
    # 将json转换为字典
    json_dict = json.loads(json_demo)

    # 遍历字典
    for (k, v) in json_dict.items():
        print(k, " : ", v)

        for data in v:
            for (data_k, data_v) in data.items():
                print("    ",data_k, " : ", data_v)