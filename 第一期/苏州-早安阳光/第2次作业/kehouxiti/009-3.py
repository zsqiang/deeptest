'''
Created on 2018年1月21日

@author: 早安阳光
'''
for i in range(100, 1000): 
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10) ** 3
        temp //= 10 # 注意这里要使用地板除哦~
    if sum == i:
        print(i)

# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3
# 因此 153 就是一个水仙花数




     




 