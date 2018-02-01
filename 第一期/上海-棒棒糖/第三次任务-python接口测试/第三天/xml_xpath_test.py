from urllib import request
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

print("解析Yahoo的XML格式的天气预报")

class Weatherxml(object):
    def __init__(self):
        self.data = {}
    #xpath提取节点,且遍历指定节点
    def getxpath(self,root,xpath_node,xpath_node_value):
        for x in root.findall('.//%s'%xpath_node):
            print(x.tag,' ',x.attrib,'',x.text)

    # 修改节点的值
    def fixvalue(self, root, xpath_node, xpath_node_value):
        for x in root.findall('.//%s' % xpath_node):
            x.text = xpath_node_value
            x.set('updated', 'yes')
        xml_update_data = ET.tostring(root, encoding="unicode")
        fp = open("Yahoo_weather_data.xml", "w")
        fp.write(xml_update_data)
        fp.close()

    #  修改节点的属性
    def fixnature(self, root, xpath_node, xpath_node_nature):
        for x in root.findall('.//%s' % xpath_node):
            x.text = xpath_node_nature
            x.set('updated', 'yes')
        xml_update_data = ET.tostring(root, encoding="unicode")
        fp = open("Yahoo_weather_data.xml", "w")
        fp.write(xml_update_data)
        fp.close()



URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
with request.urlopen(URL) as f:
    data = f.read()
root = ET.fromstring(data)

Yahoo_weather=Weatherxml()
#xpath提取节点,
print('-'*50)
Yahoo_weather.getxpath(root,'url')
#设置指定节点值
print('-'*50)
Yahoo_weather.fixvalue(root,'url','棒棒糖碰一个')
#设置指定节点的属性
print('-'*50)
Yahoo_weather.fixnature(root,'url','棒棒糖碰一个')
