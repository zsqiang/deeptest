# -*- coding:utf-8 -*-
__author__ = "Lakisha"

import json


if __name__ == "__main__":
    print("python json标准库解析实例")

    #将json文件解析为Python
    with open("json_tem.json", "r", encoding='utf-8') as fp:
        json_data = json.load(fp)

        print(json_data, type(json_data))

'''
    #将Python转化为json
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    json_data = json.dumps(data)
    json_data_format = json.dumps(data, sort_keys=True, indent=4, separators=(",", ': '))

    #打印出来看下效果
    print(data, type(data))
    print(json_data, type(json_data))
    print("将Python转化为json:", json_data_format)

    #将json转化为python
    python_data = json.loads(json_data)
    print("将json转化为python:", python_data, type(python_data))

    #将json对象字符串存文件
    fp = open('json_write.json', 'w')
    json.dump(data, fp, sort_keys=True, indent=4, separators=(',', ':'))
    fp.close()
'''
