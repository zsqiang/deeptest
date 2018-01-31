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

    def xml_find_node(self, ftype, nodetag, attrib, text):
        if ftype == "tag":
            for child in self.xml_find_root().iter(nodetag):
                return child
        if ftype == "text":
            for child in self.xml_find_root().iter(nodetag):
                while child.text == str(text):
                    return child
        if ftype == "attrib":
            for child in self.xml_find_root().iter(nodetag):
                while child.get(*attrib) == str(text):
                    return child

    def xml_node_set_text(self, text):
        # node.text = text
        # node.set('updated', 'yes')

    def xml_node_remove(self, node):
        return self.xml_find_root().remove(node)

if __name__ == "__main__":
    data = xml_parse("xml_data.xml")
    root = data.xml_find_root()
    print(root.tag)
    tag = data.xml_find_node("tag", "country", "name", "Liechtenstein")
    print(tag.attrib)
