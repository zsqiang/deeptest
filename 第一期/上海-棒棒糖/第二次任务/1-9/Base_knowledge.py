'''#学习如何注释
__author__='棒棒糖'
#该方法是一下内容无法被其他文件调用
if __name__=='__mian__':
    #这是一种注释
    sum=0
    for index in range(1,100):
        sum=sum+index #这也是注释
    print('1-99的和是:%d'%sum)

__author__='棒棒糖'
if __name__=='__main__':
    #读取键盘的输入
    data=input('请输入一串任意字符:')
    print('你输入的字符是:%s'%data)

__author__='棒棒糖'
if __name__=='__main__':
    #先获取输入
    data=input('请输入任意串字符:')
    #按照空格进行切割
    list_data=data.split(' ')
    #打印切割结果
    print(list_data)'''

__anthor__="棒棒糖"
import sys
if __name__=='__main__':
    print('命令行参数个数:%d'%len(sys.argv))
    print('命令行参数列表:%s'%str(sys.argv))
    #打印了你当前运行文件的路径
    print(sys.argv[0])





