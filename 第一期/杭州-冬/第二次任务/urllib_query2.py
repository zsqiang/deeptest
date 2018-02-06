#--coding:utf-8--
#本折继续用urllib请求电话归属查询接口,换成把参数data拼接在url后面,用get方法请求接口

import urllib.request
import json
if __name__=="__main__":
    #定义一个字典 存放传入接口的参数
    dict_para={}
    dict_para["appkey"]="55d8ae551eab404a"
    dict_para["shouji"]=13675810227

    #参数编码符合http规范
    url_data=urllib.parse.urlencode(dict_para)

    #把参数拼接在url后面
    url="http://api.jisuapi.com/shouji/query"+"?"+url_data

    #获取请求响应
    resp=urllib.request.urlopen(url)

    #读取响应主体body,返回的是一个json
    body_data=resp.read().decode('utf-8')
    print(body_data)
    
    #解析json 取出归属地 运营商等数据
    data=json.loads(body_data)
    if data["result"]!="":
        provi=data["result"]["province"]
        city=data["result"]["city"]
        compa=data["result"]["company"]
        print("归属地相关信息")
        print(provi,city,compa)
