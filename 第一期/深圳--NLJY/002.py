''''# if __name__ == '__mian__':   # 该方法时文件以下的内容无法被其他文件调用
sum = 0
for index in range(1,100):
    sum = sum +index
print('1-99的和是:%d'%sum)

data = input('请输入一个字符串:')
print('你输入的字符串是:%s'%data)

list_data = tuple(data)
print(list_data)
list_data3 = '-'.join(list_data)    # 把字符串用 '-'分隔
print(list_data3)
str_data4= data.split('g') # 以这个字符(g)为切割点
print(str_data4)
list_data1 = data.split('    ') # 按照空格进行切割
print(list_data)
'''
import sys
print('命令行参数个数：%d'%len(sys.argv))
print('命令行参数列表：%s'%str(sys.argv))
print(sys.argv[0])  #打印的是当前文件运行的路径
a = sys.argv[0]
print(a)
