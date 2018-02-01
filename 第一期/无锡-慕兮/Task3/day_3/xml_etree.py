# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

# 导入ElementTree
import xml.etree.ElementTree as ET

if __name__ == "__main__":
    print("python xml解析实例")

    data = """<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
    """

    # 载入xml的两种方式，一种从文件，一种从xml字符串
    # 注意区别：从xml字符串加载的xml直接返回root元素对象
    # 而从文件加载xml返回是xml树

    # 大家根据实际情况来决定用哪种方式即可
    # 本示例从xml字符串载入进行演示

    # 从文件加载xml，获取xml tree节点
    # tree = ET.parse('xml_data.xml')

    # 获取根节点
    # root = tree.getroot()

    # 从字符串加载xml

    # 打印下根节点的节点tag， 输出data
    root = ET.fromstring(data)
    print(root.tag)

    print("--" * 10)

    # 遍历下根节点的所有子节点及其属性
    for child in root:
        print(child.tag, " ", child.attrib)

    print("-" * 20)

    # 打印出year节点的tag和text
    for child in root.iter("year"):
        print(child.tag, " ", child.text)

    print("-" * 20)

    # 修改下节点的text试试， 把year节点所有2011修改为2017
    for child in root.iter("year"):
        if child.text == "2011":
            child.text = "2017"
            child.set('updated', 'yes')
        print(child.tag, " ", child.text)

    print("=" * 20)

    # 给每个country节点新增一个<wx>开源优测</wx>的节点试试
    for child in root.iter("country"):
        wx = ET.SubElement(child, "wx")
        wx.text = "开源优测"

    for child in root.iter("wx"):
        print(child.tag, " ", child.text)

    print("~" * 20)

    # 下面演示删除所有的neighbor节点
    # 当然你自己可以加判断条件删除指定的节点，自行尝试吧

    for child in root.findall(".//country[@name='Panama']"):
        root.remove(child)

    # 保存上述操作后的xml至xml_write_data.xml
    xml_update_data = ET.tostring(root, encoding="unicode")
    with open("xml_write_data.xml", "w", encoding="utf-8") as fp:
        fp.write(xml_update_data)