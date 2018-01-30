import hashlib
#MD5是最常见的摘要算法，速度很快，生成固定的128 bit字节，用32位的16进制字符串表示
md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
#数据量很大，可以分块多次调用update()
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
import hashlib
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

#越安全的算法不仅越慢，而且摘要长度更长,比SHA1更安全的算法是SHA256和SHA512

