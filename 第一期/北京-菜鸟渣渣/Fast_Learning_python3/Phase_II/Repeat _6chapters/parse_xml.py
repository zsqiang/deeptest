# coding=utf-8

'''

什么是ElementTree

ElementTree是Python提供解析xml的标准库，ElementTree中每个节点（即Element）具有如下属性：

tag： string对象，标识该元素类型

attrib：dictionnary对象，标识该元素属性

text：string对象，标识该元素的文本

tail：string对象，标识该元素可选的尾字符串

child elements： 标识子节点

注：Element类型是一种灵活的容器对象，用于在内存中存储结构化数据。

'''

# 使用ElementTree的标准方式为：
import xml.etree.cElementTree as ET

if __name__ == "__main__":

    print("解析本地data_demo.xml文档")
    # 加载xml文件
    tree = ET.parse("data_demo.xml")

    # 获取根节点, 并打印节点文本：data
    root = tree.getroot()
    print(root.tag)

    # 遍历输出country及其name属性
    for child in root:
        print(child.tag, "name：", child.attrib["name"])

        # 遍历rank节点
    # 我们借助iter迭代器来进行全迭代查找感兴趣的节点
    # 输出节点tag及其文本
    print("使用iter迭代器查找目标节点")
    for rank in root.iter("rank"):
        print(rank.tag, " - ", rank.text)

        # 换一种方式来遍历rank节点
    # 我们借助findall和find方法来查找感兴趣的节点
    # 输出节点tag及其文本
    # 注意：findall只能查找从当前节点的子节点查找目标节点
    print("使用findall查找目标节点")
    # 使用findall查找所有country节点，用于遍历
    for country in root.findall("country"):
        # print(country)
        # 使用find从country节点中查找rank节点
        rank = country.find("rank")
        print(rank.tag, " - ", rank.text)


        # 把所有的rank的文本都修改为： 开源优测
    for rank in root.iter("rank"):
        rank.text = "开源优测"
        rank.set('updated', 'yes')

        # 把修改后的rank的文本重新遍历打印出来，这时应该打印出： 开源优测
    for rank in root.iter("rank"):
        print(rank.text)

        # 给所有的country新增一个<url>www.testingunion.com</url>节点
    for country in root.iter("country"):
        # 创建一个节点
        url = ET.Element("url")
        # print(url)

        # 给节点url的text赋值
        url.text = "www.testingunion.com"

        # 将url节点追加到country节点下
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

    '''
     # 保存上述 修改、新增、删除后的xml到 data_demo_new.xml中
        # 大家自己打开data_demo_new.xml文档看修改、新增、删除的节点是否有效
        tree.write("data_demo_new.xml", encoding="utf-8")
    注： 用ET.fromstring("xml格式字符串") 替换ET.parse("data_demo.xml")
    ，后续其他代码不变，即可实现对xml格式的字符串进行遍历读取、新增、修改和删除动作。
    '''
    print("Element Tree XPath特性支持示例")

    # 加载xml文件
    tree = ET.parse("data_demo.xml")

    # 获取根节点, 并打印节点文本：data
    root = tree.getroot()

    # 选择当前节点, 返回的是当前节点对象列表
    print("选择当前节点")
    data = root.findall(".")
    for d in data:
        print("---->",d.tag)

        # 选择所有country节点
    print("选择所有country节点方法一")
    countrys = root.findall(".//country")
    for country in countrys:
        print(country.tag, " ", country.attrib["name"])

    print("选择所有country节点方法二")
    countrys = root.findall("country")
    for country in countrys:
        print(country.tag, " ", country.attrib["name"])

    print("选择name属性为Panama的country节点")
    countrys = root.findall(".//*[@name='Panama']")
    for country in countrys:
        print(country.tag, " ", country.attrib["name"])

        # name属性为Panama的country下的year节点
    print("name属性为Panama的country下的year节点")
    years = root.findall(".//country[@name='Panama']/year")
    for year in years:
        print(year.text)

        # 通过索引来选择country节点，选择第一个country节点
    # 注意索引从 1 开始
    print("通过索引来选择country节点，选择第一个country节点")
    country = root.findall(".//country[1]")
    for c in country:
        print(c.tag, " ", c.attrib["name"])

        # 通过子节点的文本内容来选择节点
    # 选择子节点gdppc且其文本为59900 的country节点
    # 请注意这返回的是gdppc的父节点
    print("通过子节点的文本内容来选择节点")
    gdppc = root.findall(".//*[gdppc='59900']")
    for gd in gdppc:
        print(gd.tag)

    '''
    本文就ElementTree解析xml的遍历、新增、修改、删除等操作进行了实例演示，并演示了其对XPath选择器的支持，但要注意的是其对XPath的支持是有限制的，并不支持所有的XPath语法。
    '''
