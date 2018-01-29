'''
Created on 2018年1月21日

@author: 早安阳光
'''

# remove()删除前提知道列表中有元素，但不清楚元素的具体位置
name = ["213","Python","Java","Jmeter","Selenium","LoadRunner","QTP","Appium","123","C++","VB","Ruby"]
name.remove("123")
print(name)

# del 指定位置删除,即删除最后一个
del name[-1]
print(name)

# pop() 弹出元素，默认删除最后一个元素，可以指定位置删除
name.pop()
print(name.pop())
print(name)