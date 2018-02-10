# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
urllib.request:用于构建http请求
urllib.response:用于处理http响应值得类
urllib.parse:用于url处理
urllib.error:用于错误处理
urllib.robotparser:用于处理robot.txt文件
"""
# 基于豆瓣api的爬虫

import urllib.request
import csv
import codecs
import os

if __name__ == "__main__":

    path = __file__

    # 加载xml文件
    # 切换到当前工作目录
    path_demo = os.path.dirname(path)
    os.chdir(path_demo)

    print("urllib爬取豆瓣网数据示例")
    print("搜索下关键字：Python")

    keyword = "Python"
    url = "https://api.douban.com/v2/book/search?q=" + keyword
    # print(url)
    response = urllib.request.urlopen(url)

    # print(type(response.read()))

    # 将bytes数据流解码成string
    ebook_str = response.read().decode()

    # 将string转换成dict
    ebook_dict = eval(ebook_str)

    # print(ebook_dict)

    # 获取books中的信息
    books = ebook_dict["books"]
    with codecs.open('books.csv', 'w', 'utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["书名", "作者", "描述", "出版社", "价格"])

        # 写入书籍信息
        for book in books:
            spamwriter.writerow([book["title"], 
                ",".join(book["author"]), 
                book["summary"], 
                book["publisher"], 
                book["price"]])


