#coding = utf -8

__author__ = 'Aimee'
import requests


#cookies 是存放在本地浏览器端的，一般不丢失 除非删除
# session 放在服务器端

host = 'https://httpbin.org/'
endpoint = 'cookies'
url = ''.join([host,endpoint])
params = {'show_env' :1}
url1 = 'http://www.baidu.com/'

#发送请求
r = requests.get(url)
#获取cookies
print(r.cookies)
d = requests.utils.dict_from_cookiejar(r.cookies)  #jar包转换为字典
# d = requests.utils.cookiejar_from_dict() #讲字典转换成jar包
print(d)
print({a.name:a.value for a in r.cookies})


#发送cookies到服务器

cookies = {'cookie-name':'aimee'}
r1 = requests .get(url,cookies=cookies)
print(r1.text)

#复杂的写法
s = requests.Session()
c = requests.cookies.RequestsCookieJar()
c.set('cookis-name','cookie-value',path = '/',domain = '.test.com')
s.cookies.update(c)
print(s.cookies)


