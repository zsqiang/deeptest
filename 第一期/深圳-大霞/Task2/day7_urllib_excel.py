__author__="大霞"
"""
使用urllib从网络爬取数据，写入excel进行示例演示，从豆瓣网爬取部分书籍数据，写入excel
"""
import urllib.request
from openpyxl import Workbook
if __name__=="__main__":
    print("爬取豆瓣网书籍数据写入excel实例：")

    url="https://api.douban.com/v2/book/search?q=python"
    respons=urllib.request.urlopen(url)

    #将bytes数据解码成string
    ebook_str=respons.read().decode()

    #将string数据转换成dict
    ebook_dict=eval(ebook_str)

    #构建一个WorkBook对象
    wb=Workbook()#激活一个sheet
    ws=wb.active#写入表头
    ws.append(["书名","作者","描述","出版社","价格"])
    #写入书信息
    for book in ebook_dict["books"]:
        ws.append([book["title"],
                   ",".join(book["author"]),
                   book["summary"],
                   book["publisher"],
                   book["price"]])
    #保存
    wb.save("ebook.xlsx")

