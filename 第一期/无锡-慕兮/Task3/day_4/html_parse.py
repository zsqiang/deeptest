# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

from html.parser import HTMLParser
import http.client

class BlogHTMLParser(HTMLParser):
    data = []
    data_key = ""

    def __init__(self):
        HTMLParser.__init__(self)
        self.is_a = False

    def handle_starttag(self, tag, attrs):
    # 处理开始为a的标签
        if tag == "a":
            self.is_a = True
            for name, value in attrs:
                if name=="href":
                    # 提取a的href属性值
                    self.data_key = value

    def handle_data(self, data):
    # 处理结束为a的标签
        if self.is_a and self.lasttag == "a":
            # 将a标签的href属性值作为key， a的文本作为data构建字典
            self.data.append({self.data_key: data})


    def handle_endtag(self, tag):
        #处理a结束表情
        if self.is_a and self.lasttag == "a":
            self.is_a = False

    def get_data(self):
        #返回所有从a中提取到的目标数据
        return self.data

if __name__ == "__main__":
    print("python HTML解析实例")

    print("访问博客园，获取首页html源码")

    #构建博客园链接
    conn = http.client.HTTPSConnection("www.cnblogs.com")

    # 获取博客园首页html源码
    conn.request("GET", "/")
    rl = conn.getresponse()
    data = rl.read().decode(encoding="utf-8")
    # print(data)

    # 解析博客园首页html源码，提取所有a的href和文本数据
    blogHtmlParser = BlogHTMLParser()
    blogHtmlParser.feed(data)
    links = blogHtmlParser.get_data()

    print(links)
    
'''
    运行__init__初始化实例

    执行handle_starttag

    执行handle_data

    handle_endtag

    重复2、3、4直至把所有的a提取完毕
'''