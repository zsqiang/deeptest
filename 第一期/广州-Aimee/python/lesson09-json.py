#coding = utf-8
__author__ = 'Aimee'

#json.dumps 将python对象编码成json字符串, 返回json串
#json.loads将已编码的json串解码为python对象，返回python对应的数据类型
import json

# print("json转dict")
# json_str = '{"name":"百度","url":"www.baidu.com","id":"test"}'
# #查看类型
# print("原类型：",type(json_str))
#
# #转成dict对象
# json_dict = json.loads(json_str)
# print("转换后的类型:",type(json_dict))
# print(json_dict)
#
# #遍历字典
# for (k,v) in json_dict.items():
#     print(k,":",v)
#
#
#
#
# #dict字典转json
# json_dict = {
#     "name":"百度",
#     "url":"www.baidu.com",
#     "id":"test"
# }
#
# print("原类型：",type(json_dict))
#
# json_str = json.dumps(json_dict)
# print("转换后的类型：",type(json_str))
# print(json_str)

if __name__ == "__main__":
    print("json串解析")
    json_demo ='''{
        "微信":[
            {
                "name":"百度",
                "uid":"test",
                "desc":"分享开源技术"
            },
            {
                "name":"百度1",
                "uid":"test11",
                "desc":"分享开源技术1"

            },
            {
                "name":"百度2",
                "uid":"test2",
                "desc":"分享开源技术2"
            }
        ],
        "web":[
            {
                "url":"www.baidu.com",
                "name":"BAIDU",
                "desc":"分享开源"
            },
            {
              "url":"www.baidu.com",
                "name":"BAIDU",
                "desc":"分享开源"
            }
        ]
    }'''

#将json转换成字典
json_dict = json.loads(json_demo)

print(json_dict)

print('\n')

#遍历字典
for (k,v) in json_dict.items():
    #输第一层级
    print(k,":",v)
    for data in v:
        #遍历列表
        for (data_k,data_v) in data.items():

            print(data_k,":",data_v)
