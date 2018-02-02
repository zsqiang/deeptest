#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

'''
什么是INI格式

INI文件格式是某些平台或软件上的配置文件的非正式标准，以节(section)和键(key)构成，常用于微软Windows操作系统中。这种配置文件的文件扩展名多为INI，故名。

INI是英文“初始化”（initialization）的缩写。正如该术语所表示的，INI文件被用来对操作系统或特定程序初始化或进行参数设置。

INI文件格式

节(section) 节用方括号括起来，单独占一行，例如：

[section]

键(key)

键(key)又名属性(property)，单独占一行用等号连接键名和键值，例如：

name=value

注释(comment)

注释使用英文分号（;）开头，单独占一行。在分号后面的文字，直到该行结尾都全部为注释，例如：

; comment text

'''

'''
Python ConfigParser类

在python里由标准模块ConfigParser模块提供的ConfigParser类实现对INI格式的文件进行读写，下面我们看看其主要的函数，也是大家必须熟悉的。


'''
from configparser import  ConfigParser
import  os

if __name__ == '__main__':
    # 初始化
    cf = ConfigParser()  # 读取ini文件,path为要读取的ini文件的路径
    cf.read("ini_data.ini",encoding='utf-8')

    # 获取所有sections。即将配置文件中所有“[ ]”读取到列表中
    s = cf.sections()
    logging.info(s)
    # 获取指定section的options。

    # 即将配置文件某个section内key 读取到列表中
    o = cf.options("mysql")  # 获取指定section 的配置信息v = cf.items("msyql")# 按照类型读取指定section 的option 信息# 同样的还有getfloat、getbooleandb_host = cf.get("mysql", "host")
    logging.info(o)

    db_port = cf.getint("mysql", "port")

    db_user = cf.get("mysql", "user")

    db_pass = cf.get("mysql", "password")

    # 设置某个option 的值。（记得最后要保存）
    cf.set("mysql", "password", "654321")

    # 添加一个section。（同样要保存）
    cf.add_section('oracle')

    cf.set('oracle', 'host', '127.0.0.1')
    cf.set('oracle', 'port', '5555')

    logging.info(cf.options('mysql'))
    logging.info(cf.options('oracle'))


    #
    # #  移除section 或者option (同样要保存)
    # cf.remove_option('oracle', 'port')
    # cf.remove_section('oracle')

