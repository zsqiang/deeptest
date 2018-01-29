#-*-coding:utf-8 -*-
import json
if __name__ == "__main__":
    print("dict 转json")
    json_dict = {
        "name" : "张晋",
        "member_id":"2345345",
        "sex":"男"
    }
    print("原类型：",type(json_dict))
    #将字典转换成json串，会被转换成字符类型
    json_str = json.dumps(json_dict)
    print("转换后的类型：",type(json_str))
    print(json_str) 