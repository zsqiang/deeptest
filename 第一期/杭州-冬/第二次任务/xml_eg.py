#--cooding:utf-8--
#本折关于用py来解析xml文件,涉及一些前端基础
#<tag name=attribute>text</tag>--比较简单的一个 标签的构成
import xml.etree.ElementTree as ET

if __name__=="__main__":
    #把磁盘上xml文件读进来作为一个对象
    xml_py=ET.parse("xml_data.xml")

    #获得根节点即：<data>
    root=xml_py.getroot()
    print(root.tag)

    #遍历子节点country:有3个不同name的country
    for coun in root:
        print("tag:",coun.tag,"name:",coun.attrib["name"])

    #查找tag为year的节点：用迭代器
    for tag_year in root.iter("year"):
        print("tag:",tag_year.tag,"text:",tag_year.text)

    #用findall find查找--findall在当前节点子节点查找,注意二者区别 字如其名
    ##要找到year先要找到其父节点
    for coun2 in root.findall("country"):  #父节点
        rank= coun2.find("rank")    #在每个父节点下找year
        print("tag2:",rank.tag,"text2:",rank.text)

    #上面findall可以直接替换成for循环,因为它查找的是第一层子节点country
    """
    for country5 in root:
        rank= coun5.find("rank")
        print("tag2:",rank.tag,"text2:",rank.text)
    """
    #修改所有tag为rank的text
    for rank3 in root.iter("rank"):
        rank3.text="py3"
        rank3.set("update","yes")

    for rank4 in root.iter("rank"):
        print(rank4.text)

    #在所有country节点下增加一个子节点：<month>01</month>
    for coun3 in root.iter("country"):
    #for coun3 in root
        #创建一个节点
        mon1=ET.Element("month")
        #给该节点text一个值
        mon1.text="01"
        #将该节点加到 country节点下
        coun3.append(mon1)

    #测试下上面新增 看是否输出
    for add_mon in root.iter("month"):
        print(add_mon.tag,add_mon.text)

    #删除gdppc text值为13600的节点
    for country in root.findall("country"):
        #gdpcc=country.find("gdpcc")
        #if str(gdpcc.text)=="13600":

        if country.find("gdppc").text=="13600":
            country.remove(country.find("gdppc"))
    #测试下是否删除
    for gd in root.iter("gdppc"):
        print(gd.text)

    #若要将上述修改写入到磁盘文件:write()
    xml_py.write("xml_data2.xml",encoding="utf-8")

    #总结：增加 删除 改动需以查找为基础,查找三种方式 iter()迭代器 findall for循环 