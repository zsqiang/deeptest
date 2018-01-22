#-*- coding:utf-8 -*-
import json
if __name__ == "__main__":
 print("json转dict")
 json_str= '{"name":"zhangjin","member_id":"sa1234234","sex":"男"}'
    #原类型
 print("原类型：",type(json_str))
 #转成dict类型
 json_dict = json.loads(json_str)
 print("转换后的类型：",type(json_dict))
 #遍历字典
 for(k,v) in json_dict.items():
     print(k,":",v)
