from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read() #f.read()JSON 数据
print('Status:', f.status, f.reason)
for k, v in f.getheaders(): #f.getheaders()HTTP 响应的头
    print('%s: %s' % (k, v))
print('Data:', data.decode('utf-8'))

#模拟 iPhone 6 去请求豆瓣首页：
from urllib import request
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
for k, v in f.getheaders():
    print('%s: %s' % (k, v))
print('Data:', f.read().decode('utf-8'))

