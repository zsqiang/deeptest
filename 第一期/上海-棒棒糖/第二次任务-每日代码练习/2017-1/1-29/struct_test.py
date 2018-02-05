import struct
# struct.pack(fmt, v1, v2, ...)
# struct.unpack(fmt, buffer)

# format
# <         little-endian
# >         big-endian
# c         char            (1 byte)
# I         unsigned int    (4 bytes)
# H         unsigned short  (2 bytes)

# 编写一个bmpinfo.py，可以检查任意文件是否是位图文件，
# 如果是，打印出图片大小和颜色数
def bmp_check(file):
    with open(file,'rb') as f:
        bs=f.read(30)
        print(bs)
        ts=struct.unpack('<ccIIIIIIHH', bs)
        print(ts)
    if ts[0] == b'b' and ts[1] == b'x14':
        print('File Type: bmp')
        print('size:%d*%d' % (ts[6], ts[7]))
        print('colors:%d' % ts[9])
    else:
        print('File Type: unknown')
bmp_check('goodread.bmp')
bmp_check('bb.bmp')
bmp_check('goodread.png')