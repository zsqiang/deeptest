# -*- coding:utf-8 -*-
import codecs
import csv
import urllib
import urllib.request
# try:
#     import xml.etree.cElementTree as ET
# except ImportError:
#     import  xml.etree.ElementTree as ET
#
# __author__ = 'beck'
# if __name__ == '__main__':
#     print("解析本地demoxml的文件：")
#     tree = ET.parse("demoxml.xml")
#     #获取到根节点，并打印节点文本:data
#     root = tree.getroot()
#     print("根节点为：%s"%root.tag)
#     #打印country和name的属性
#     for child in root:
#         print(child.tag,"name",child.attrib["name"])
#     #变量rank节点，并使用iter变量节点内容和输出文本内容
#     print("利用iter迭代器来输出相关内容：")
#     for rank in root.iter("rank"):
#         print(rank.tag,"-",rank.text)
#     #利用findall和find的方法来遍历rank节点
#     print("使用findall方法来遍历：")
#     for rank in  root.findall("country"):
#         rankone = rank.find("rank")
#         print(rankone.tag,"-",rankone.text)
#     #修改所有的rank的对应的text的值
#     for rank in root.iter("rank"):
#         rank.text = u"开源优测"
#         rank.set('update','yes')
#     #输出修改后的内容
#     for rank in  root.iter("rank"):
#         print(rank.text)
#     #在所有的country节点下新增<url>www.testingunion.com</url>的解决
#     for country in  root.iter("country"):
#         url = ET.Element("url")
#         url.text = "www.testingunion.com"
#         #将url新增到country节点下面
#         country.append(url)
#     #将每个country节点的url打印出来
#     for country in  root.iter("country"):
#         url = country.find("url")
#         print("更新后结果为:%s"%url.text)
#     #删除year节点的内容：
#     for country in root.iter("country"):
#         year = country.find("year")
#         if year is not None:
#             print("删除了year节点")
#             #country.remove(year)
#     #选择当前节点，返回的是当前对象的列表
#     print("选择为当前节点的对象：")
#     data = root.findall(".")
#     for d in  data:
#         print(d.tag)
#     print("选择所有的country节点的方法一：")
#     countrys = root.findall("country")
#     for country in  countrys:
#         print("country节点的值：",country.tag,":",country.attrib["name"])
#     print("选择所有的country节点的方法二：")
#     countrys = root.findall(".//country")
#     for country in  countrys:
#         print("country节点信息",country.tag,":",country.attrib["name"])
#     print("选择name属性为Panama的country节点：")
#     countrys = root.findall(".//*[@name='Panama']")
#     for country in  countrys:
#         print(country.tag,":",country.attrib["name"])
#     print("选择name属性为Panama的country下year节点：")
#     years = root.findall(".//country[@name='Panama']/year")
#     for year in years:
#         print(year.text)
#     print("通过索引来选择country节点，选择第一个country节点:")
#     country = root.findall(".//country[1]")
#     for index in country:
#         print(index.tag,":",index.attrib["name"])
#     print("通过子节点的文本内容来选择节点:")
#     gdppc = root.findall(".//*[gdppc='141100']")
#     for gc in gdppc:
#         print(gc.tag,":",gc.attrib["name"])

    #urllib模块的练习
# def gethtml(url):
#     page = urllib.request.urlopen(url)
#     html = page.read()
#     return  html
#
# html = gethtml("https://tieba.baidu.com/index.html")
# print(html)
if __name__ == '__main__':
    # print("urllib爬取豆瓣网数据示例")
    # print("搜索下关键字： Python")
    # url = "https://api.douban.com/v2/book/search?q=python"
    # #url ="https://www.douban.com/search?q = python"
    #
    # reponese = urllib.request.urlopen(url)
    # #将btyes字节流转换为string
    # ebook_str = reponese.read().decode()
    # #将string转换为dict
    # ebook_dict = eval(ebook_str)
    # #print(ebook_str)
    # #print(type(ebook_dict))
    #
    # count = ebook_dict['count']
    # total = ebook_dict['total']
    # with codecs.open('books.csv','w','utf_8 with BOM') as csvfile:
    #     #对需要写入csv文件的内容做个规范定义
    #     spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     #这是第一页的所获取的书籍信息
    #     spamwriter.writerow(["书名", "作者", "描述", "出版社", "价格"])
    #     for book in ebook_dict["books"]:
    #         spamwriter.writerow([book["title"],",".join(book["author"]),book["summary"],book["publisher"],book["price"]])
    #     #从第2页开始写入书籍信息
    #     for start in  range(1,int(total/count)+1):
    #         url = "https://api.douban.com/v2/book/search?q=python&start=%d" % start
    #         try:
    #             reponese = urllib.request.urlopen(url)
    #         except:
    #             print("爬的太多了，不允许继续爬了")
    #             break
    #         ebook_str = reponese.read().decode()
    #         ebook_dict = eval(ebook_str)
    #         for book in  ebook_dict["books"]:
    #             spamwriter.writerow([book["title"],",".join(book["author"]),book["summary"],book["publisher"],book["price"]])
    # print("总计搜索了 %d 本书的信息" % total)

    print("urllib实例演示：")
    url = "https://www.baidu.com"
    response = urllib.request.urlopen(url)
    print("打印下请求返回的header")
    print(response.headers)
    print("打印下状态码对应的可读性文字说明，例如在http协议里，200 对应 OK")
    print(response.reason)
    print("打印下状态码")
    print(response.status)
    print("打印下请求返回的数据")
    print(response.read().decode('utf-8'))
