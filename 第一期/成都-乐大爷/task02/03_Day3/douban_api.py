# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
图书api说明：https://developers.douban.com/wiki/?title=book_v2#get_book_tags
requests：http://docs.python-requests.org/en/master/
任务说明：实现一个基本的爬虫，从利用豆瓣API爬取python相关数据信息，
包括但不限于：书名、作者、定价、摘要等等，并将这些信息格式化到excel文档中
https://api.douban.com/v2/book/search?q=python&count=1
"""
import requests
import xlwt
import json
   
    
# 将结果存入一个list中，再将list写入excel

payload = {'q': 'python', 'count': 4}
wb = xlwt.Workbook()
ws1 = wb.add_sheet('Python')

r = requests.get("https://api.douban.com/v2/book/search", params=payload)
# print(type(r.text))
book_infos = r.json()
# print(type(book_infos))     # 类型为字典
# print(book_infos['books'])
book_info = []
L = ['序号' , '书名', '作者', '出版日期', '评分', '价格', '简介']
for data in book_infos['books']: 
   
    average = data['rating']['average']
    subtitle = data['subtitle']
    author = data['author']
    pubdate = data['pubdate']
    summary = data['summary']
    price = data['price']
    book_info.append([subtitle, author, pubdate, average, price, summary])

# print(book_info[0][0])
# print("*"*10)
# print(book_info[1])
for i in range(len(L)):
    ws1.write(0,i,L[i])

for k in range(len(book_info)):
    ws1.write(k+1,0,k+1)
    for j in range(len(book_info[k])):
        # print(book[0])
        ws1.write(k+1,j+1,book_info[k][j])
        
wb.save('books.xls')

print('end')


