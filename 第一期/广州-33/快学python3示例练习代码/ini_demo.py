# coding = utf-8
# 生成一个ini文件，并写入数据，然后再读取出来显示。

# 导入模块

import configparser

if __name__ == "__main__":
    # 先构建一个对象
    config = configparser.ConfigParser()

    # 先让我们写几组数据
    # 先新增一个section

    config.add_section("第一部分")

    # 在新增的section下加key-value键值对
    config.set("第一部分", "性别", "女")
    config.set("第一部分", "星座", "水瓶座")
    config.set("第一部分", "城市", "广州")

    # 再新增一个section，但不加key-value键值对
    config.add_section("第二部分")

    # 写入文件
    with open('iniConfig.ini', 'w') as configfile:
        config.write(configfile)

    # 下面开始我们把刚才的ini文件读出来看看
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
        for option in options:
            print("[%s] %s=%s" % (sec, option, config.get(sec,option)))