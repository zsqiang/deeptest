# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

import xml.etree.ElementTree as ET

class xml_parse():

    def __init__(self, data):
        self.data = data

    # def read_xml(self, data):
    #     self.data = data
    #     return data

    def xml_find_root(self):
        data = self.data
        if "." in data:
            tree = ET.parse(data)
            root = tree.getroot()
        else:
            root = ET.fromstring(data)
        return root

    def xml_findall_node(self,nodetag):
        for child in self.xml_find_root().findall(nodetag):
            return child

    def xml_find_node_bytag(self, nodetag):
        for child in root.iter(nodetag):
                return child

    def xml_find_node_bytext(self, nodetag, text):
        for child in root.iter(nodetag):
                while child.text == str(text):
                    return child

    def xml_find_node_byattrib(self, nodetag, attrib, text):
        for child in root.iter(nodetag):
                while child.get(attrib) == str(text):
                    return child


    def xml_find_node_byxpath_rn(self, xpath_rep, attrib, attribvalue):
        for node in root.findall(xpath_rep):
            if attrib == "tag" and node.tag == attribvalue:
                return node
            if attrib == "text" and node.text == attribvalue:
                return node
            if attrib == "attrib" and node.attrib == attribvalue:
                return node

    def xml_find_node_byxpath(self, xpath_rep, attrib, *attribvalue):
        for node in root.findall(xpath_rep):
            if attrib == "tag":
                return node.tag
            if attrib == "text":
                return node.text
            if attrib == "attrib":
                return node.attrib
            if attrib == "attrib_text":
                return node.get(*attribvalue)

    def xml_set_node_byxpath(self, xpath_rep, attrib,  value, attribute=None):
        node = root.find(xpath_rep)
        if attrib == "text":
            node.text = str(value)
            node.set('updated', 'yes')
        if attrib == "attrib":
            node.set(attribute, value)
            # node.attrib = {attribute, value}
            # node.set('updated', 'yes')

    def xml_node_remove(self, xpath_fep, xpath_cep):
        fnode = root.find(xpath_fep)
        for node in fnode.findall(xpath_cep):
            fnode.remove(node)
        # fnode = list(root.find(xpath_fep))
        # cnode = root.find(xpath_cep)
        # print(fnode)
        # fnode.remove(cnode)
        # print(list(fnode))

    def xml_getchildnode(self):
        pass


if __name__ == "__main__":

    data = xml_parse("xml_data.xml")
    root = data.xml_find_root()
    print(root.tag)

    '''
    node1 = data.xml_find_node_byattrib("country", "name", "Liechtenstein")
    node2 = data.xml_find_node_bytext("year", "2011")
    node3 = data.xml_find_node_bytag("country")
    print(node1.attrib, node2.text, node3.attrib)
    # data.xml_node_remove("year")
    # node4 = data.xml_findall_node("year")
    # print(node4)
    '''
    #修改属性值
    print(data.xml_find_node_byxpath("country[@name='Panama']", "attrib"))
    data.xml_set_node_byxpath("country[@name='Panama']", attrib="attrib", attribute="name", value="Chinese")

    #修改文本值
    print(data.xml_find_node_byxpath(".//year", attrib="text"))
    data.xml_set_node_byxpath(".//year", attrib="text", value="2017")

    #删除节点
    data.xml_node_remove(".//country[@name='Liechtenstein']", ".//year[@updated='yes']")

    print(data.xml_find_node_byxpath(".//year", attrib="attrib"))

    #写入修改后的文本内容
    xml_update_data = ET.tostring(root, encoding="unicode")
    with open("xml_write_data.xml", "w", encoding="utf-8") as fp:
        fp.write(xml_update_data)
