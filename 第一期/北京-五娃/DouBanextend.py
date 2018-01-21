# __author__ ='wuwa'
# -*- coding: utf-8 -*-
# url = "https://api.douban.com/v2/book/search?q=python&start=%d" % start
import json
import requests
from openpyxl import Workbook

url = "https://api.douban.com/v2/book/search?q=python"
response = requests.get(url)
douban_str = response.text
print(type(json.loads(douban_str)))
# 将相应结果转换为dict
douban_dict = json.loads(douban_str)
count = douban_dict["count"]
total = douban_dict["total"]
books = douban_dict["books"]

wb = Workbook()
ws = wb.active
ws.append(["title", "alt_title", "author", "author_intro", "summary", "publisher", "price"])
for start in range(1, int(total / count) + 1):
    pass

for child_dict in books:
    title = child_dict['title']
    alt_title = child_dict['alt_title']
    author = child_dict['author']
    author_intro = child_dict['author_intro']
    summary = child_dict['summary']
    publisher = child_dict['publisher']
    price = child_dict['price']
    # print(type(title), type(alt_title), type(author), type(author_intro), type(summary), type(publisher), type(price))
    # 需要将author转换为string
    ws.append([title, alt_title, ','.join(author), author_intro, summary, publisher, price])



wb.save("extend1.xlsx")
