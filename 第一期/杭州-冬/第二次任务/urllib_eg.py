#--coding:utf-8--
#本折关于http的urlllib库

#在py里有三个咚咚--http.client  urllib  requests.这三个都是py用来处理实现了http协议的一些东西,如我们每天看见的网页
#都是http https开头

#三个咚咚作用很相似.其中client更底层,一般使用起来比较麻烦.另外两个更高级,使用起来更加方便直观友好
#好似做一个家具 client就是把树切割-打磨-打蜡-组装一步步来.另外两个就是需要的原料都给你准备好,你直接组装就行了

import urllib.request

#看到博客网一篇文章不错,现在我用py来获取它的一些信息
if __name__=="__main__":
    #目标文章网址
    url_eg="https://www.cnblogs.com/flowingwind/p/8379881.html"

    #访问该网页
    respose=urllib.request.urlopen(url_eg)
    #输出访问后的响应结果：当然不是你眼睛看到的文字,而是浏览器认识的html源码
    html_eg=respose.read()
    #print(html_eg)

    #获取相应的其他信息 如header
    header_eg=respose.info  #返回的是一个对象代表该header,不是具体信息,用于其他请求中
    print(header_eg)

    #说人话 输出具体的header信息
    header_eg2=respose.getheaders()
    for i,j in header_eg2:  #header信息常存于dict这种结构中
        print(i,":",j)


    #获取响应的状态码
    status_num=respose.getcode()
    print(status_num)   #200 说明服务器响应了我们的访问请求

    #把url输出来
    url=respose.geturl()
    print(url)