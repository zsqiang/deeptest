# _*_ coding : utf-8 _*_
__author__ = "Jason"
'''
概述：
    ini是我们常见到的配置文件格式之一。
    ini是微软Windows操作系统中的文件扩展名（也常用在其他系统）。
    ini是初始化（Initial）的缩写。正如该术语所表示的，INI文件被用来对操作系统或特定程序初始化或进行参数设置。

其基本组成形式如下：
[section_1]
key1 = value1
key2 = value2
key3 = value3
key4 = value4

[section_2]
key1 = value1
key2 = value2
key3 = value3
key4 = value4

    我们通过Python的ConfigParser模块来对ini文件进行读写操作。

ConfigParser
    读取：
    read(fileName)              读取ini文件内容
    sections()                  获取所有section，并以列表的形式返回
    options(sections)           获取指定section的所有option
    get(section,option)         获取section中option的值，返回为String类型。
    
    写入
    set(section,option,value)   对section中的option进行更新
'''
import configparser

if __name__ == "__main__":
    #先构造一个对象
    config = configparser.ConfigParser()

    #写入几组数据
    #先新增一个section
    config.add_section("开源优测")

    #在新增的section下增加key-value键值对
    config.set("开源优测","微号","DeepTest")
    config.set("开源优测","口号","自我娱乐")
    config.set('开源优测','号外','自律使我自由')

    #再增加一个section，但不加key-value键值对
    config.add_section("section_add")

    #写入文件
    with open("iniConfig.ini","w") as configfile:
        config.write(configfile)

    #读取文件
    config.read("iniConfig.ini")

    #获取文件中所有section
    sections = config.sections()
    print(sections)

    #通过section获取option
    for sec in sections:
        options = config.options(sec)
        print(options)

    #通过section和option获取对应的value值
    for sec in sections:
        for option in config.options(sec):
            print("[%s]%s=%s"%(sec,option,config.get(sec,option)))