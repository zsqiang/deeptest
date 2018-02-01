#--coding:utf-8--
#本折关于解析html
#涉及html构成相关,标签和xml很相似

#用py来解析html,要用到一个类--HTMLParser
#我们要用它时,需要写一个类去继承,并复写相应的标签处理方法。遇到相应标签里的数据,它会自动调用相应方法去处理

from urllib import request
from html.parser import HTMLParser

class Mypaser(HTMLParser):
    #定义一个列表和一个空字符串 用于后面存放我们的数据
    data=[]
    data_keyvalue={}
    attri_value=""

    def __init__(self):
        HTMLParser.__init__(self)
        self.judge_a=False

    def handle_starttag(self,tag,attris,):
        if tag=="a":
            self.judge_a=True
            for name,attri in attris:
                if name=="href":
                    self.attri_value=attri

    def handle_data(self,data):
        if self.judge_a and self.lasttag=="a":
            self.data_keyvalue[self.attri_value]=data
            self.data.append(self.data_keyvalue)

    def handle_endtag(self,tag):
        if self.judge_a and self.lasttag=="a":
            self.judge_a=False

    def get_data(self):
        return self.data

if __name__=="__main__":
    r=request.urlopen("https://www.cnblogs.com/flowingwind/p/8379881.html")
    html_data=r.read().decode(encoding='utf-8')

    mypaser1=Mypaser()
    mypaser1.feed(html_data)
    result=mypaser1.get_data()
    print(result)