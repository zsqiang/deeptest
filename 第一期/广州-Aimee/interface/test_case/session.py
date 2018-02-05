#coding = utf -8
__author__ = 'Aimee'

#session 是客户端与服务器之间的会话，用来保存用户的信息

import requests


host = 'https://httpbin.org/'
endpoint = 'cookies/set/sessioncookie/123456789'
url = ''.join([host,endpoint])
url1 = 'https://httpbin.org/cookies'
#发送请求
# r = requests.get(url1)
# print(r.text)
#
# session = requests.Session() #初始化session对象
# session.get(url)               #cookies的信息存在session中
# r1 =session.get(url1)
# print(r1.text)

header1 = {'test1':'aa'}
header2 = {'test1':'bb'}

session1 =requests.Session()
#已经存在服务器中的信息
session1.headers.update(header1)
#发送新的header信息
r2 = session1.get('https://httpbin.org/headers',headers =header1)
print(r2.text)
#删除已经存在的会话信息 赋值none
session1.headers['test1'] = None
r3 = session1.get('https://httpbin.org/headers',headers =header2)
print(r3.text)

