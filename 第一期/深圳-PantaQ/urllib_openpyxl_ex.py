# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urllib_openpyxl_ex
   Description :
   Author :       PantaQ
   date：          2018/1/26
-------------------------------------------------
   Change Activity:
                   2018/1/26:
-------------------------------------------------
"""

# 在叶子的例子上稍作修改

import urllib.request
from openpyxl import Workbook

if __name__ == "__main__":
    print("爬取豆瓣网书籍数据写入excel示例")

    # 通过豆瓣网搜索API，搜索python关键词，采集书籍数据
    # 本示例只采集第一页的数据
    # url = "https://api.douban.com/v2/book/search?q=python"
    # response = urllib.request.urlopen(url)

    # 将bytes数据流解码成string
    # ebook_str = response.read().decode()

    # 将string转换成dict
    # ebook_dict = eval(ebook_str)

    # 构建一个Workbook对象
    wb = Workbook()
    # 激活第一个sheet
    ws = wb.active
    # 写入表头
    ws.append(["书名", "作者", "翻译者", "页数", "描述", "出版社", "价格", "ISBN", "出版日期", "作者简介",
               "封面地址", "目录"])

    count = 20
    total = 1496

    for start in range(1, int(total / count) + 1):
        url = "https://api.douban.com/v2/book/search?q=python&start=%d" % start
        try:
            response = urllib.request.urlopen(url)
        except:
            print("别老爬别人的数据，要爬也别太快，会被封IP的")
            break

        ebook_str = response.read().decode()

    # 将string转换成dict
        ebook_dict = eval(ebook_str)
    # 写入书信息
        for book in ebook_dict["books"]:
            ws.append([book["title"],
                ",".join(book["author"]),         #为啥需要",".join还没有想明白
                ",".join(book["translator"]),
                book["pages"],
                book["summary"],
                book["publisher"],
                book["price"],
                book["isbn13"],
                book["pubdate"],
                book["author_intro"],
                book["images"]["large"],
                book["catalog"]])

    # 保存
    wb.save("ebook.xlsx")
    print("总计搜索了 %d 本书的信息" % total)

    # 共采集1496本书的信息，excel表格数据304KB