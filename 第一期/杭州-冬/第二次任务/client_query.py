#--coding:utf-8--
#本折用更底层的client来实现电话归属接口的查询 可用get post方法实现
#下面用get实现 可能有些地方涉及http的request response的构造的基础知识
#接口地址 http://api.jisuapi.com/shouji/query

import http.client
import urllib.parse
import json
if __name__=="__main__":
    #实例化一个http连接对象
    conn=http.client.HTTPSConnection("www.jisuapi.com")
    #把请求接口的参数存放在字典
    data={"appkey":"55d8ae551eab404a","shouji":13675810226}

    #同样把请求接口的参数拼接在url之前,先要用urlencode使得其符合http规定形式
    para=urllib.parse.urlencode(data)

    #把参数拼接在url后面,注意格式 用？分割
    url="http://api.jisuapi.com/shouji/query"+"?"+para

    #发送http请求
    conn.request("GET",url)     #GET大写

    #获取请求的响应
    resp=conn.getresponse()
    #输出响应相关信息
    print(resp.status,resp.reason)

    #输出响应主体body--json格式
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

