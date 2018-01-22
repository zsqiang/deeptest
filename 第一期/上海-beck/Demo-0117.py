# -*- coding:utf-8 -*-
import configparser
__author__ = 'beck'

if __name__ == '__main__':
    #先创建一个对象
    config = configparser.ConfigParser()
    #写入几组数据，新增一个section
    config.add_section("Test For Python")
    #在新增的section下新增key，vlaue的值
    config.set("Test For Python","one","TestOne")
    config.set("Test For Python","two","TestTwo")
    config.set("Test For Python","three","TestThree")
    #新增另一个section
    config.add_section("Java Test")
    #进行写的操作
    with open("iniConfig.ini",'w')as configfile:
        config.write(configfile)
    #进行读的操作并打印
    config.read("iniConfig.ini")
    section = config.sections()
    print(section)

    #获取指定的section的所有option
    mylist = config.sections()
    for sec in mylist:
        option =config.options(sec)
        print(option)
    #通过get方法来获取所有section对应的option的值
    for sec in  mylist:
        for option in config.options(sec):
            print("[%s] %s=%s"%(sec,option,config.get(sec,option)))

if __name__ == '__main__':
    conf = configparser.ConfigParser()
    conf.read("test.conf")
    #直接读取section对应的值
    name = conf.get("section1","name")
    print(name)
    age = conf.get("section1","age")
    print(age)
    #获取所有的sections
    sections = conf.sections()
    print(sections)
    #写入值
    conf.set("section2","port","8090")
    conf.set("section2","IEPort","80")

    conf.add_section("new_section")
    conf.set("new_section","URL","http://www.baidu.com")
    conf.write(open("test.conf","w"))
if __name__ == '__main__':
    f = open("test.txt",'a',encoding='UTF-8')
    f.write(u"\n测试使用数据第三次测试")
    f.close()
    f1 = open("test.txt",'r')
    file = open("test.txt",'w+')
    file.write(u"第一次测试使用数据!!!\n")
    file.write(u"第二次测试使用数据!!!!\n")
    file.write(u"第三次测试使用数据!!!!!\n")
    file.flush()
    file.close()
    file2 = open("test.txt",'r')
    print(file2.readable())
    tuple1 = file2.readlines()
    print(tuple1)
    for lines in  tuple1[:]:
        print(lines)
    print(file2.tell())
    print(file2.seek(0))
    file2.close()