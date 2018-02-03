#--coding:utf-8--
#本折关于py用来处理http的三大库中的client

#client主要用HTTPConnection HTTPResponse来处理http相关交互

#初始化建立一个目标http连接
HTTPConnection(host,port=None,[timeout,]source_address=None)

#连接到初始化时指定服务器.若客户端还没有连接到服务器,默认在发出请求时间自动调用该方法
HTTPConnection.connect()

#关闭连接 HTTPConnection.close()

#发送HTTP请求
#HTTPConnection.request(method,url,body=None,headers={},encode_chunked=None)

#将数据发送到服务器,在头信息之后--endheader() 获取响应前--getresponse()
HTTPConnection.send(data)
#获取请求的响应--一个HTTPResponse对象 可迭代对象
HTTPConnection.getresponse()

#设置调试级别 有问题方便定位 默认为0 即是不输出调试信息
HTTPConnection.set_debudlevel(level)

#返回响应主体
HTTPResponse.read()
HTTPResponse.read(200) #每次读200个字节并返回

#返回头信息
HTTPResponse.getheaders()
#返回指定头信息 无则返回默认
HTTPResponse.getheader(name,defaul=None)

#返回状态码和reson描述
HTTPResponse.status
HTTPResponse.reason

#将响应主体下一个字节读取到缓冲区XX 返回读取的字节数
HTTPResponse.readinto(XX)

#
#import http.client
from http import client
if __name__=="__main__":

    #建立一个目标http连接并连接到目标服务器
    conne=client.HTTPSConnection('www.baidu.com')

    #get请求获取目标资源
    conne.request('get','/')
    r0=conne.getresponse()
    print(r0.status)
