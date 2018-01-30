'''
Created on 2018年1月21日

@author: 早安阳光
'''
name = ["Python","Java","Jmeter","Selenium","LoadRunner","QTP","Appium"]
print(name)
# 取出元素
name[2]       
print (name[2]) 

# 把"LoadRunner"和"Appium" 对调位置
name[4],name[6] = name[6],name[4]
print(name)

