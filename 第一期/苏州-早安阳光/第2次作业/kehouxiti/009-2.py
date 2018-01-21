'''
Created on 2018年1月21日

@author: 早安阳光
'''
# break语句的作用是终止当前循环，跳出循环体。
# continue语句的作用是终止本轮循环并开始下一轮循环（这里要注意的是：在开始下一轮循环之前，会先测试循环条件）

while True:
    while True:
        break
        print(1)
    print(2)
    break  # 因为 break 只能跳出一层循环，记住咯！
print(3)



# 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内
# break语句的作用是终止当前循环，跳出循环体。
# continue语句的作用是终止本轮循环并开始下一轮循环（这里要注意的是：在开始下一轮循环之前，会先测试循环条件）
count = 3
mima = '170417'
while count:
    pwd = input('请输入密码：')
    if pwd == mima:
        print('密码正确，进入程序^^')
    elif '*' in mima:
        print('密码中不能含有"*"号！您还有',count,'次机会！',end ='')
        continue
    else:
        print('密码输入错误！您还有',count -1,'次机会！',end ='')
    count -= 1
    