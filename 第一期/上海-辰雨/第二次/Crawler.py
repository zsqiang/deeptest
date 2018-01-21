#!/usr/bin/env python
# encoding: utf-8
from bs4 import BeautifulSoup
import requests

r = requests.get('http://www.cnblogs.com/yoyoketang/')
'''请求首页获取整个html界面'''
blog = r.content
'''用html.parser解析html'''
soup = BeautifulSoup(blog,'html.parser')
'''获取所有的class属性为dayTitle,返回Tag类'''
times = soup.find_all(class_='dayTitle')
for i in times:
	print i.a.string

descs = soup.find_all(class_='postCon')
for i in descs:
	#先获取div这个Tag类，tag的 .contents属性可以将tag的子节点以列表的方式输出
	print i.div.contents[0]  #这个是获取列表中的第一项
	print '*'*35
	#这个是在div 标签下面的a 标签里面的内容。可以顺接写
	print i.div.a.contents[0]

title = soup.find_all(class_='postTitle')
for i in title:
	print i.a.string












