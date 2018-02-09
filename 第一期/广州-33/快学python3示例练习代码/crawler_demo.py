# coding = utf-8
# 使用豆瓣网的API进行数据爬虫

import urllib.request
import csv
import codecs

if __name__ == "__main__":
    print("urllib爬取豆瓣网数据示例")
    print("搜索下关键字：Python")

    url = "https://api.douban.com/v2/book/search?q=python"
    response = urllib.request.urlopen(url)

    # 将bytes数据流解码成string
    ebook_str = response.read().decode()

    # 将string转换成dict
    ebook_dict = eval(ebook_str)

    count = ebook_dict["count"]
    total = ebook_dict["total"]

    with codecs.open('books.csv', 'w', 'utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["书名", "作者", "描述", "出版社", "价格"])
        # 写书信息
        for book in ebook_dict["books"]:
            spamwriter.writerow([book["title"], ",".join(book["author"]), book["summary"], book["publisher"], book["price"]])