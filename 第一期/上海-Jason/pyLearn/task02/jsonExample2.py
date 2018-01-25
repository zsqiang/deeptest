# _*_ coding : utf-8 _*_
__author__ ="Jason"

import json

if __name__ == "__main__":
    print("JSON转dict")

    json_str =  '{"name":"test","key2":"value2"}'

    #原类型
    print("原类型：",type(json_str))#原类型： <class 'str'>

    #转换成dict对象，会被转换成字典dict类型
    json_dict = json.loads(json_str)
    print("JSON转换后的类型：",type(json_dict))#JSON转换后的类型： <class 'dict'>
    print(json_dict)#{'name': 'test', 'key2': 'value2'}

    #无需转码
    json_str1 = {"name":"测试"}
    print(json_str1)#{'name': '测试'}