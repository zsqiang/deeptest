#--coding:utf-8--
#本折关于用urllib来请求接口 查询号码归属地

#网上找了个接口 输入电话号码可查询归属地
#接口地址 http://api.jisuapi.com/shouji/query

from urllib import request
import urllib.request
if __name__=="__main__":
    #定义一个字典 存放传入接口的参数
    #参数名一定要和接口文档一致,随意更改可导致错误
    dict_para={}
    dict_para["appkey"]="55d8ae551eab404a"  #访问接口的一个凭证,若需要,请自己注册获取
    dict_para["shouji"]=13675810228

    #参数要在http上传输 必须符合一个规范即 application/x-www-form-urlencoded形式
    #利用urlencode()可达到该效果  返回ASCII编码的字符串
    url_para=urllib.parse.urlencode(dict_para)

    #现在虽然符合http规范 但要传进urlopen().还要进一步编码成bytes,因为urlopen()中data参数类型之一为bytes
    bytes_para=url_para.encode('utf-8')

    #构造一个request对象.或者省去该步直接传入到urlopen()
    req=urllib.request.Request("http://api.jisuapi.com/shouji/query")

    #发送请求获得响应
    resp=urllib.request.urlopen(req,bytes_para)

    #读取并返回响应的body
    body_data=resp.read().decode('utf-8')
    print(body_data)
    #返回的格式是json

#上述接口请求凭证为个人注册获得,有次数限制，如需要请到网上注册获得
#上述把参数作为data单独传递 应该是用的Post方法.也可用get方法 把参数拼接在url后面