# 0-100间 所有偶数和
sum = 0
print('计算0-100间所有偶数和')
for i in range(0,101,2):# 因为是要求偶数  所有要几个2
    sum +=i
print(sum)

# 打印99乘法表
i =1
while i <10:
    j = 1
    while j<=i:
        print('%d*%d=%d\t'%(j,i,i*j),end = '')
        j += 1
    print('')
    i += 1

varl = int(input('请输入一个整数:'))
if varl >0 and varl<10:
    print('你输入的是一个大于0，小于10的数')
elif varl >=10:
    print('你输入的数大于或等于10')
else:
    print('你输入的为负数')

for i in range(5):
    #print(i ,end=' ') # 不换行
    #print(i,end='\n')   # 换行
    print(i,end = '\t') # 空格
