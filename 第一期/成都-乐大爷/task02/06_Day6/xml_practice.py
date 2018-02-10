# -*- coding:utf-8 -*-

__author__ = 'catleer'

import os

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

if __name__ == '__main__':
    print("解析本地data_demo.xml文档")

    path = __file__

    # 加载xml文件
    # 切换到当前工作目录
    path_demo = os.path.dirname(path)
    os.chdir(path_demo)
    tree = ET.parse("date_demo.xml")
    root = tree.getroot()

    print(root.tag)

    # 遍历输出父元素下的子元素及其属性
    for child in root:
        print(child.tag, "name: ", child.attrib["name"])

    # 遍历rank节点
    # 输出节点tag及文本
    print("使用iter迭代器查找目标节点")
    for rank in root.iter("neighbor"):
        print(rank.tag, " - ", rank.attrib["name"], rank.text)
    
    # 使用findall或find查找感兴趣的节点,需要逐级查找
    print("使用findall查找目标节点")
    for country in root.findall("country"):
        rank = country.find("rank")
        print(rank.tag, " - ", rank.text)

    # 修改xml文件中元素的文本
    for rank in root.iter("rank"):
        rank.text = "Deeptest"
        # 设置rank的属性为updated，属性值为yes
        rank.set('updated', 'yes')

    # 给所有的country新增一个节点：<url>www.testingunion.com</url>节点
    for country in root.iter("country"):
        url = ET.Element("url")

        url.text = "www.testingunion.com"
        country.append(url)
    
    # 打印下整个xml出来看看是不是所有country节点都新增了一个url节点
    for country in root.iter("country"):        
        # 查找url节点
        url = country.find("url")        

        # 打印url的text
        print(url.text)    
    
    # 删除year节点
    for country in root.iter("country"):
        year = country.find("year")    
        
        # 如果year节点存在，则删除
        if year is not None:
            print("删除了一个year节点")
            country.remove(year) 

    tree.write("data_demo_new.xml", encoding="utf-8")

    