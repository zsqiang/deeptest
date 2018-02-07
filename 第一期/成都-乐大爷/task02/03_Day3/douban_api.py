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


# # def wirte_excel(*K):
#     wb = xlwt.Workbook()
#     ws1 = wb.add_sheet('Python')

#     alignment = xlwt.Alignment() # Create Alignment
#     alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL,HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED,HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
#     alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP,VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED

#     pattern = xlwt.Pattern() # Create the Pattern
#     pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN,SOLID_PATTERN, or 0x00 through 0x12
#     pattern.pattern_fore_colour = 5 # May be: 8 through 63. 0 = Black,1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7= Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = DarkYellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = LightGray, 23 = Dark Gray, the list goes on...

#     borders = xlwt.Borders() # Create Borders
#     borders.left = xlwt.Borders.MEDIUM_DASHED  # May be: NO_LINE, THIN, MEDIUM,DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED,THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED,MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through0x0D.
#     borders.right = xlwt.Borders.MEDIUM_DASHED 
#     borders.top = xlwt.Borders.MEDIUM_DASHED 
#     borders.bottom = xlwt.Borders.MEDIUM_DASHED 
#     borders.left_colour = 0x40
#     borders.right_colour = 0x40
#     borders.top_colour = 0x40
#     borders.bottom_colour = 0x40

#     style = xlwt.XFStyle() # Create the Style
#     style.alignment = alignment
#     style.pattern = pattern
#     style.borders = borders
#     # style.alignment = alignment # Apply the Font to the Style
    
    
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


