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
        for child in self.xml_find_root().iter(nodetag):
                return child

    def xml_find_node_bytext(self, nodetag, text):
        for child in self.xml_find_root().iter(nodetag):
                while child.text == str(text):
                    return child

    def xml_find_node_byattrib(self, nodetag, attrib, text):
        for child in self.xml_find_root().iter(nodetag):
                while child.get(attrib) == str(text):
                    return child


    def xml_find_node_byxpath(self, xpath_rep, attrib, *attribvalue):
        for node in self.xml_find_root().findall(xpath_rep):
            if attrib == "tag":
                return node.tag
            if attrib == "text":
                return node.text
            if attrib == "attrib":
                return node.attrib
            if attrib == "attrib_text":
                return node.get(*attribvalue)

    def xml_set_node_byxpath(self, xpath_rep, attrib, *attribute, value):
        node = self.xml_find_root().find(xpath_rep)
        if attrib == "text":
            node.text = value
            node.set('updated', 'yes')
        if attrib == "attrib":
            node.set(*attribute, value)


    def xml_node_set_text(self, text):
        pass


    def xml_node_remove(self, node):
        for child in self.xml_find_root().findall(node):
            root.remove(child)

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
    print(data.xml_find_node_byxpath("country[@name='Panama']", "attrib"))
    print(data.xml_find_node_byxpath(".//year", attrib="text"))
    data.xml_set_node_byxpath(".//year", attrib="text", value="2017")
    print(data.xml_find_node_byxpath(".//year", attrib="text"))

    xml_update_data = ET.tostring(root, encoding="unicode")
    with open("xml_write_data.xml", "w", encoding="utf-8") as fp:
        fp.write(xml_update_data)