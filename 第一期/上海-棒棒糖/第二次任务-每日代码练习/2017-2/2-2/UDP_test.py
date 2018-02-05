import socket
#创建socket,SOCK_DGRAM指定的类型是UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',9999))
#接收来自客户端的数据
print('Bind UDP on 99999')
while True:
    #接收数据:
    data,addr=s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
#例子简单,这里省掉了多线程