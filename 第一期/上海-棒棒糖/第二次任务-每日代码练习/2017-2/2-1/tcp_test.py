# 导入 socket 库:
import socket
# 创建一个 socket:
# AF_INET6是IPv6，SOCK_STREAM 指定使用面向流的 TCP 协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection:close\r\n\r\n')
# 接收数据:
buffer = []
while True:
# recv(max)方法每次最多接收指定的字节数，在while循环下不断调用，直到recv()返回空数据
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接:
s.close()
#把 HTTP 头和网页分离一下，把 HTTP 头打印出来，网页内容保存到文件
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)

