关于client.httpsconnection()中url的不同输入的一些问题
1.1
if __name__=="__main__":
    conne=client.HTTPSConnection('baidu.com')

    conne.request('GET','/')

    resp=conne.getresponse()

    print(resp.reason,resp.status)
    for i,j in resp.getheaders():
        print(i,':',j)

--------------------------------------
结果是：
Moved Temporarily 302
Server : bfe/1.0.8.18
Date : Sun, 04 Feb 2018 09:50:34 GMT
Content-Type : text/html
Content-Length : 161
Connection : keep-alive
Location : http://www.baidu.com/

1.2  改下url

conne=client.HTTPSConnection('www.baidu.com')
--------------------------------------------------
OK 200
Accept-Ranges : bytes
Cache-Control : no-cache
Connection : Keep-Alive
Content-Length : 14720
Content-Type : text/html
Date : Sun, 04 Feb 2018 10:16:14 GMT
Last-Modified : Mon, 22 Jan 2018 07:46:00 GMT
P3p : CP=" OTI DSP COR IVA OUR IND COM "
Pragma : no-cache
Server : BWS/1.1
Set-Cookie : BAIDUID=E7E40A05FC43884DA548D5D78B1CD14A:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie : BIDUPSID=E7E40A05FC43884DA548D5D78B1CD14A; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie : PSTM=1517739374; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Vary : Accept-Encoding
X-Ua-Compatible : IE=Edge,chrome=1

1.3
conne=client.HTTPSConnection('www.baidu.com')
conne.request('GET','http://tieba.baidu.com') #一定是GET大写
----------------------------------------------
ok 200

1.4
conne=client.HTTPSConnection('www.baidu.com')
conne.request('GET','tieba.baidu.com')
----------------------------------------------
Bad Request 400

1.5
conne=client.HTTPConnection('www.qq.com')
conne.request('GET','sports.qq.com/nba/')
--------------------------------------------
Bad Request 400
Server : squid/3.5.24
Date : Sun, 04 Feb 2018 10:43:43 GMT
Content-Type : text/html
Content-Length : 173
Connection : close

1.6
conne=client.HTTPConnection('www.qq.com')
conne.request('GET','http://sports.qq.com/nba/')
-------------------------------------------------
OK 200
Server : squid/3.5.24
Date : Sun, 04 Feb 2018 10:45:34 GMT
Content-Type : text/html; charset=GB2312
Transfer-Encoding : chunked
Connection : keep-alive
Vary : Accept-Encoding
Expires : Sun, 04 Feb 2018 10:47:34 GMT
Cache-Control : max-age=120
X-Cache : from www-hy
Vary : Accept-Encoding
Vary : Accept-Encoding
Content-Encoding : gzip
Vary : Accept-Encoding
X-Cache : MISS from shenzhen.qq.com

总结：查看首页是http 还是https 再实例化对应连接
    创建连接实例 参数host不用加上http/https 但要加www
    用get、post等访问后续网页,记得用浏览器检查其真实链接,
    网页上显示的链接常是最后的重定向后的地址,而不是第一步的跳转链接