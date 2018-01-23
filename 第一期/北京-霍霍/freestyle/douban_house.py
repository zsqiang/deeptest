# -*- coding:utf-8 -*-
__author__ = "huohuo"

import urllib.request
import csv
import codecs
import ssl

if __name__ == "__main__":
    print("urllib爬取豆瓣网房源数据示例")
    #print("搜索下关键字：Python")
    
    headers={  
            'Host':'ptlogin2.qq.com',  
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'  
        } 
    context = ssl._create_unverified_context()
    url = "https://api.douban.com/group/259273/"
    response = urllib.request.urlopen(url,context = context, headers = headers)
    
    start = response.find(r'<table class= "olt">')
    end = response.find(r'</table>')
    response1 = language[start, end]
    # 将bytes数据流解码成string
    ehouse_str = response1.read().decode()

    # 将string转换成dict
    ehouse_dict = eval(ehouse_str)
    
    
    title = ehouse_dict["title"]
    #href = ehouse_dict["total"]

    with codecs.open("houses.csv", 'w', 'utf_8_sig') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["标题"])
        # 写书信息
        for title in ehouse_dict["title"]:
            spamwriter.writerow([title["title"],
            ",".join(title["title"])])
            #book["summary"],
           # book["publisher"],
           # book["price"]])

        # 从第二页开始，获取其他书籍信息
        """  

        for start in range(1, int(total / count) + 1):
            url = "https://api.douban.com/v2/book/search?q=python&start=%d" % start
            try:
                response = urllib.request.urlopen(url)
            except:
                print("爬数据啦，哈哈")
                break

            # 将bytes数据转化成string
            ebook_str = response.read().decode()

            # 将string转化成dict
            ebook_dict = eval(ebook_str)

            # 输出书籍信息
            for book in ebook_dict["books"]:
                spamwriter.writerow([book["title"],
                ",".join(book["author"]),
                book["summary"],
                book["publisher"],
                book["price"]])
        """
    #print("总计搜索了 %d 本书的信息" % total)

        