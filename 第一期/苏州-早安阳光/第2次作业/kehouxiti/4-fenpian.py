'''
Created on 2018年1月21日

@author: 早安阳光
'''
shiwu = ["韭菜","菠菜","胡萝卜","鸡蛋","牛奶","猪肉","豆腐","青菜","鱼","羊肉","洋葱","土豆","西红柿"]
# 取1到9的数据
print(shiwu[0:10])
# 取1到5的数据
print(shiwu[:6])
# 从4开始取数据
print(shiwu[4:])
# 取全部的数据
print(shiwu[:])

# 列表分片进阶玩法
print(shiwu[0:12:2])
print(shiwu[::2])
print(shiwu[1::2])