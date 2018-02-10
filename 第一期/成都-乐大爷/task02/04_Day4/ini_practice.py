# -*- coding:utf-8 -*-

__author__ = 'catleer'

"""
[section_1]
key1 = value1
key2 = value2

[section_2]
key1 = value1
key2 = value2
key3 = value3

"""

import configparser

if __name__ == '__main__':
    # 构建一个对象
    config = configparser.ConfigParser()
    # 添加一份section
    section_1 = "开源优测"
    config.add_section(section_1)

    # 在新增的section中添加key-value键值对，ini文件中每个section下的格式Wie键值对
    # set写入进行更新：set( section, option, value)
    config.set(section_1, "微号", "DeepTest")
    config.set(section_1, "口号", "坚持的小宝贝才有糖吃，哈哈")
    config.set(section_1, "号外", "大师不止一个号")

    # 再新增一个section
    section_2 = "这个一个没有键值对的"
    config.add_section(section_2)

    # 写入文件
    with open('iniConfig.ini', 'w') as configfile:
        config.write(configfile)

    # 再读取这个文件
    config.read("iniConfig.ini")

    # 获取文件中所以的section
    sections = config.sections()
    print("输出section的名称:", sections)

    # 获取section下的所以的options
    for sec in sections:
        options = config.options(sec)
        print(options)

    # 根据sections和options获取对应的value值
    for sec in sections:
        for option in config.options(sec):
            print("[%s] %s=%s " % (sec, option, config.get(sec, option)))

    