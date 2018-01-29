# _*_ coding : utf-8 _*_
__author__ = "Jason"

'''
概述
    urllib是Python是最基础、最核心的HTTP协议支持库，
    诸多第三方库都依赖urllib，所以urllib是必须掌握的HTTP库。
    
    掌握urllib有利于;
    1.深入理解HTTP协议
    2.可以更好的学习和掌握第三方HTTP库
    3.快速的开展基于HTTP的接口测试
    4.快速进入爬虫学习之路
urllib组成
    我们一起看下urllib由哪些模块或类构成：
    urllib.request                  用于构建http请求
    urllib.response                 用于处理http响应值的类
    urllib.parse                    用于url处理
    urllib.error                    用于错误处理
    urllib.robotparser              用于处理robot.txt文件
    
基本功能实例
import urllib.request
if __name__ == "__main__":    
    print("urllib基本实例")
    url = "http://www.baidu.com"
    # 访问下百度
    response = urllib.request.urlopen(url)    
    # 打印下状态码
    print(response.status)    
    # 打印下状态码对应的可读性文字说明，例如在http协议里，200 对应 OK
    print(response.reason)    
    # 打印下请求返回的header
    print(response.headers)    
    # 打印下请求返回的数据
    print(response.read().decode("utf-8"))
    
爬取数据实例
    基于豆瓣网的API的实例：
    豆瓣网的API网址：
    https://developers.douban.com/wiki/?title=guide
'''
import urllib.request
import csv
import codecs

if __name__ == "__main__":
    print("urllib爬取豆瓣网数据示例")
    print("搜索下关键字：Python")

    url = "https://api.douban.com/v2/book/search?q=python"
    response = urllib.request.urlopen(url)
    # print(response)#<http.client.HTTPResponse object at 0x00000000031E6908>
    print(type(response))#<class 'http.client.HTTPResponse'>

    # 将bytes数据流解码成string
    ebook_str = response.read().decode()
    print(ebook_str)
    print(type(ebook_str))#<class 'str'>

    # 将string转换成dict
    ebook_dict = eval(ebook_str)
    print(ebook_dict)
    print(type(ebook_dict))#<class 'dict'>

    count = ebook_dict["count"]
    total = ebook_dict["total"]
    print(count)#20
    print(total)#1496

    with codecs.open('books.csv','w','utf-8') as csvFile:
        spamwriter = csv.writer(csvFile,delimiter=',',quotechar = '|',quoting = csv.QUOTE_MINIMAL)

        spamwriter.writerow(["书名","作者","描述","出版社","价格"])

        # 写入书信息
        for book in ebook_dict['books']:
            spamwriter.writerow([book['title'],",".join(book["author"]),book["summary"],book["publisher"],book["price"]])

        #print(ebook_dict)
        # 从第2页开始，获取其他书籍信息
        # 这段代码采集了大量数据，容易被封IP，所以注释了
        '''
        for start in range(1, int(total / count) + 1):
            url = "https://api.douban.com/v2/book/search?q=python&start=%d" % start
            try:
                response = urllib.request.urlopen(url)
            except:
                print("别老爬别人的数据，要爬也别太快，会被封IP的")
                break

            # 将bytes数据流解码成string
            ebook_str = response.read().decode()

            # 将string转换成dict
            ebook_dict = eval(ebook_str)

            # 输出书籍信息
            for book in ebook_dict["books"]:
                spamwriter.writerow([book["title"],
                                     ",".join(book["author"]),
                                     book["summary"],
                                     book["publisher"],
                                     book["price"]])
         '''
    csvFile.close()
    print("总计搜索了 %d 本书的信息" % total)