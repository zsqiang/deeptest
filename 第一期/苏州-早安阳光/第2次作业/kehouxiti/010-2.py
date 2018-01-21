'''
Created on 2018年1月21日

@author: 早安阳光
'''
# 要求1：输出member
# 要求2：member列表每个元素换行输出
# 要求3：member列表每行打印显示姓名和成绩

member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

#要求1打印
print(member) 

#要求2打印

for each in member:
    print(each)

#要求3打印-方法1：
count = 0 
length = len(member) #len() 方法返回列表元素个数
while count < length:
    print(member[count],member[count + 1])
    count += 2 #  等同于 count=count + 2

#要求3打印-方法2：
    
for each in range(len(member)): #len() 方法返回列表member的元素个数，即10个元素
#     print(each) #打印(0,10)
    if each % 2 ==0:
        print(member[each],member[each + 1])

