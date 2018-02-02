import xml.etree.ElementTree as etree

weatherxml = etree.parse('yahooweather.xml')
tree = weatherxml.getroot()
for root in tree:
    #  print root  #channel 直接的一级子元素
    pindao = tree.findall('channel')
    des = pindao[0].find('title')
    print(des.text)
    for elem in tree.iter(tag='pubDate'):  # iter() 深度优先搜素遍历
        print(elem.text)
    for elem in tree.iter(tag='{http://xml.weather.yahoo.com/ns/rss/1.0}condition'):
        print(elem.attrib)
    for elem in tree.iter(tag='{http://xml.weather.yahoo.com/ns/rss/1.0}forecast'):
        print(elem.attrib)
