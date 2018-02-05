#打印语句
print('你好，这是我的第一个python3程序')

#简答的运算
a = 10
b = 20

if a-b>0:
    print("a大于b")
elif a-b==0:
    print("a等于b")
else:
    print('a小于b')

#脚本模式
if __name__=='__main__':
    sum=0
    for index in range(1,100):
        sum=sum+index
    print('1-99的和为:%d'%sum)
