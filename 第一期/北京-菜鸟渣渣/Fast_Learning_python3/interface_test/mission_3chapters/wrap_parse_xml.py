''''
概述

什么是XML？

XML 指可扩展标记语言（eXtensible Markup Language）。 XML 被设计用来传输和存储数据。

XML是一套定义语义标记的规则，这些标记将文档分成许多部件并对这些部件加以标识。

它也是元标记语言，即定义了用于定义其他与特定领域有关的、语义的、结构化的标记语言的句法语言。


xml 构成:
1.DOM document object model  文档对象模型
2.ElementTree  元素数
3.SAX  simple API for xml
SAX (simple API for XML )
python 标准库包含SAX解析器，SAX用事件驱动模型，通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件。

DOM(Document Object Model)
将XML数据在内存中解析成一个树，通过对树的操作来操作XML。

ElementTree(元素树)
ElementTree就像一个轻量级的DOM，具有方便友好的API。代码可用性好，速度快，消耗内存少。

'''
import xml.etree.ElementTree as ET

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")


class ParseXml:
    def __init__(self, data):
        self.data = data

    def loadFromFile(self):
        # 从data加载返回root元素对象
        tree = ET.parse("xml_data.xml")
        # 获取根节点
        root = tree.getroot()
        logging.info(root.tag)
        return root

    def _loadFromStr(self):
        # 从data加载返回root元素对象
        root = ET.fromstring(self.data)
        logging.info(root.tag)

        # 遍历下根节点的所有子节点及其属性

        for child in root:
            print(child.tag, " ", child.attrib)
        # 找所有的year节点玩下
        for child in root.iter("year"):
            print(child.tag, " ", child.text)

        return root

    def _updateXML(self):
        root = self._loadFromStr()
        for child in root.iter("year"):

            if child.text == "2011":
                logging.info(">>>>>>>>>>>>>>>")
                child.text = "2017"

        for child in root.iter("year"):
            logging.info((child.tag, child.text))

    def _insertXml(self):
        root = self._loadFromStr()
        for child in root.iter("country"):
            wx = ET.SubElement(child, 'wx')
            wx.text = "ACBC"

        for child in root.iter("wx"):
            logging.info((child.tag, child.text))

        return root

    def _delteXml(self):
        root = self._loadFromStr()

        for child in root.iter("wx"):
            print(child.tag, child.text)
            root.remove(child)
            print(child.tag, child.text)

        return root

    def _saveFile(self):
        xml_update_data = ET.tostring(self._insertXml(), encoding="unicode")  # 写入xml_write_data.xml
        import codecs
        fp = codecs.open("xml_write_data", "w", "utf-8")

        fp.write(xml_update_data)

        fp.close()


if __name__ == '__main__':
    data = '''
        <data>
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
         '''
    parsexml = ParseXml(data)
    # parsexml.loadFromFile()
    # parsexml.loadFromStr()
    parsexml._updateXML()
    parsexml._insertXml()
    parsexml._saveFile()
