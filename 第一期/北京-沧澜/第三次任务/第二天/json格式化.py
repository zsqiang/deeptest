#-*- coding:utf-8 -*-
__author__ = '张晋'

import json

if __name__ == "__main__":
    print('json格式化实例')
    data = [{'a':1,'b':2,'c':3,'d':4,'e':5}]
    json_data = json.dumps(data,sort_keys=True,indent=4,separators=(',',':'))
    #打印格式化的字符串
    print(json_data)
