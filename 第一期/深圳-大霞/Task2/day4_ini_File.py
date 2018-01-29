"""
INI文件读写
ConfigParser
读取
read(filename) 读取ini文件内容
sections() 获取所有的section，并以列表的形式返回
options(sections) 获取指定section的所有option
get(section,option) 获取section中option的值，返回为string类型
写入
set( section, option, value) 对section中的option进行更新
"""
import configparser
if __name__=="__main__":
    #先构建一个实例对象
    config=configparser.ConfigParser()

    config.add_section("开源优测")

    #写入几组数据，新增session
    config.set("开源优测","微型","DeepTest")
    config.set("开源优测","口号","娱乐娱乐")
    config.set("开源优测", "号外", "其实我开了好多号")

    # 再新增一个section，但不加key-value键值对
    config.add_section("新增session")

    #写入文件
    with open("iniConfig.ini",'w') as configfile:
        config.write(configfile)

    # # 下面开始我们来把刚才的ini文件读出来看看
    config.read("iniConfig.ini")
    # 获取它的所有section
    sections = config.sections()
    print(sections)

    # 获取section下所有的options
    for sec in sections:
        options = config.options(sec)
        print(options)

        # 根据sections和options获取对应的value值
    for sec in sections:
        for option in config.options(sec):
            print("[%s] %s=%s " % (sec, option, config.get(sec, option)))