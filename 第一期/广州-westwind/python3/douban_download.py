#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/20 23:20
# @Author  : caijiangchun
# @Site    : 
# @File    : douban_download.py
# @Software: PyCharm
import urllib.request
from openpyxl import Workbook
import openpyxl
import time

def douban_data():

    url = "https://api.douban.com/v2/book/search?q=python"

    response = urllib.request.urlopen(url)

    ebook_str = response.read().decode()

    ebook_dict = eval(ebook_str)

    count = ebook_dict["count"]
    total = ebook_dict["total"]

    for start in range(0 , total//count):

        url = "https://api.douban.com/v2/book/search?q=python&start=%s" %start

        response = urllib.request.urlopen(url)

        ebook_str = response.read().decode()

        ebook_dict = eval(ebook_str)

        wb = openpyxl.load_workbook("douban.xlsx")
        sheet = wb.get_sheet_by_name("Sheet1")

        if start == 0:
            sheet.append(["书名", "作者", "出版社", "价格"])

        for book in (ebook_dict["books"]):

            sheet.append([book["title"],
                       ",".join(book["author"]),
                       book["publisher"],
                       book["price"]])
            time.sleep(5)
        wb.save("douban.xlsx")



if __name__ == "__main__":

    douban_data()
