# -*- coding:utf-8 -*-
__author__="大霞"
#XML解析处理，Element Tree
#对data_demo.xml文档进行读、增、修改、删除操作
try:
    # 若想加快速度，可以使用C语言编译的API xml.etree.cElementTree。
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElemenTree as ET

if __name__=="__main__":
    print("解析本地的data_demo.xml文件")
    #加载xml文件
    tree = ET.parse("data_demo.xml")
    #获取根节点，并打印节点文本data
    root=tree.getroot()
    print(root.tag)

