#coding=utf-8


# __author__ = 'Aimee'

import xml.etree.ElementTree as ET

print ("解析本地data_demo.xml文档")

# 加载xml文件
tree = ET.parse("data_demo.xml")
#获取根节点，并打印节点文本：data
root = tree.getroot()
print (root.tag)

#遍历输出country及其name属性
for child in root:
    print (child.tag,"name:",child.attrib["name"])

# 遍历rank节点，借助iter迭代器来进行全迭代查找感兴趣的节点
#输出节点tag及其文本
# print ("使用iter迭代器查找目标节点")
# for rank in root.iter("rank"):
#         print (rank.tag,"-",rank.text)

#使用findall和find方式查找节点
#使用findall查找所有country节点，用于遍历
# print ("使用findall查找目标节点")
# for country in root.findall("country"):
#     # print (country.tag,country.attrib["name"])
#     #使用find从country节点中查找rank节点
#     rank = country.find("rank")
#     print (rank.tag,"-",rank.text)


#把所有的rank文本修改为：开源优测
for rank in root.iter("rank"):
    rank.text = "开源优测"
    rank.set('update','yes')
#修改后再打印rank内容
for rank in root.iter("rank"):
        print (rank.text)

#给所有的country新增一个<url>www.baidu.com</url>
for country in root.iter("country"):
    #创建一个节点
    url = ET.Element("url")
    # print (url)
    #给节点url的text赋值
    url.text = 'www.baidu.com'
    #讲url节点追加到country节点下
    country.append(url)

#打印新增的uil节点
for country in root.iter("country"):
    url = country.find("url")
    print (url.text)

#删除year节点
for country in root.iter("country"):
    year = country.find("year")
    #如果year节点存在 则删除
    if year is not None :
        print ("删除了一个year节点")
        country.remove(year)

tree.write("data_demo_new1.xml",encoding="utf-8")











