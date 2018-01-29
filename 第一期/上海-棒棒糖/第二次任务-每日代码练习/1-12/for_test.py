#range函数使用
for i in range(5):
    print(i,end=",")
#换行
print('')
for i in range(0,10,2):
    print(i,end=',')
print('')

#打印99乘法表
for i in range(1,10):
    for j in range(i,10):
        print('%d*%d=%d'%(i,j,i*j),end=' ')
    print('')
print('')

#打印三角形
for i in range(1,10):
    print('*'*i,end='\n')


