# -* coding:utf-8 *-
__author__ = 'nancy'

from base import xmlop

if __name__ == "__main__":
    # path  = "readini.ini"
    # conf = iniconf(path)
    # print(conf.get_conf_data("addsection"))

    xml = "xml_date.xml"
    xmltest = xmlop(xml)
    print(xmltest.get_xml_data("index", "login"))
