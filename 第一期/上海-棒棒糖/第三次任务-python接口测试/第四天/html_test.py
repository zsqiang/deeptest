from html.parser import HTMLParser
import  http.client

class BlogHTMLPareer(HTMLParser):
    data=[]
    data_key=''
    def __init__(self):
        #HTMLParser可以接收相应的HTML内容，并进行解析，遇到HTML的标签会自动调用相应的handler（处理方法）来处理
        HTMLParser.__init__(self)
        self.is_a=False  #标志，用以标记是否找到我们需要的标签

    def handle_starttag(self, tag, attrs):
        #HTMLParser.handle_starttag(tag, attrs)：对开始标签的处理方法
        if tag=='a':
            self.is_a=True
            for name,value in attrs:
                if name =='href':
                    self.data_key=value

    def handle_data(self, data):
        # 对标签之间的数据的处理方法
        if self.is_a and self.lasttag=='a':
            self.data.append({self.data_key : data})

    def handle_endtag(self, tag):
        #对结束标签的处理方法
        if self.is_a and self.lasttag=='a':
            self.is_a=False

    def get_data(self):
        return self.data

print("python HTML解析实例")
print("访问博客网，获取首页html源码")
# 构建链接
conn=http.client.HTTPSConnection('www.cnblogs.com')
# 获取html源码
conn.request('GET','/')
r1=conn.getresponse()
data=r1.read().decode(encoding='utf-8')


# 解析html源码，提取所有a的href和文本数据
blogHtmlParser=BlogHTMLPareer()
blogHtmlParser.feed(data) #HTMLParser.feed(data)：接收一个字符串类型的HTML内容，并进行解析
#links=blogHtmlParser.get_data()

for item in blogHtmlParser.data:
    print('---------------')
    for k,v in item.items():
        print("%s : %s" % (k,v))









