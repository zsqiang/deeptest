#coding=utf-8
from __future__ import print_function
import ConfigParser

if __name__ == "__main__":
    config = ConfigParser.ConfigParser()

    config.add_section('Section1')
    config.set('Section1', 'an_int', '15')
    config.set('Section1', 'a_bool', 'true')
    config.set('Section1', 'a_float', '3.1415')

    config.add_section('Section2')

    with open('iniConfig.ini','w') as configfile:
        config.write(configfile)


    #读取ini文件
    config.read("iniConfig.ini")
    sections = config.sections()
    print(sections)
    
    #提取option值
    for sec in sections:
        options = config.options(sec)
        print(options)
    
    #提取option对应的value值
    for sec in sections:
        for option in config.options(sec):
            print("[%s] %s=%s" %(sec,option,config.get(sec,option)))