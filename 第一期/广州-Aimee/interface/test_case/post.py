#coding = utf -8
__author__ = 'Aimee'

#params ,headers, data,json,files
import requests
import json

host = 'https://httpbin.org/'
endpoint = 'post'
url = ''.join([host,endpoint])
params = {'show_env' :1}

#对应postman body中的form-data形式
data = {'a':"aimee",'b':'学测试'}

r = requests.post(url,params=params,data=data)
print(r.text)

res = r.json()
print(res)
# print(res['form'])


#json 对应postman中 body中 raw格式将json格式复制进去

# data = {
# "employees": [
# { "firstName":"Bill" , "lastName":"Gates" },
# { "firstName":"George" , "lastName":"Bush" },
# { "firstName":"Thomas" , "lastName":"Carter" }
# ]
# }

# r = requests.post(url,data=data)  #直接传无效
# print(r.text)

# r = requests.post(url,data=json.dumps(data)) #低版本
# r = requests.post(url,json=data)  #request模块高版本支持json关键字参数
# print(r.text)
# resp =r.json()
# employees =resp.get('data')
# print(employees)
# print(type(employees))
# print(response['json'])


#files
#1.普通上传文件
# files = {'files':open('test.txt','rb')}
#2、通过文件上传字符串
# files = {'files':('test.txt','aimee is a tester')}
#3、自定义文件名、文件类型以及请求头（请求文件名称、文件路径、文件类型、文件请求头）
# files = {'files':open('江湖.jpg','rb')}
# files = {'files':('江湖.jpg',open('江湖.jpg','rb'),'image/png')}

#4、传送多个文件
# files = [
#     ('field1',('test.txt',open('test.txt','rb'))),
#     ('field2',('江湖.jpg',open('江湖.jpg','rb'),'image/png'))
#
# ]

#5、流式上传
# with open('test.txt') as f:
#     r = requests.post(url,data=f)

# r = requests.post(url,files=files)
# print(r.headers)
# print(r.text)


