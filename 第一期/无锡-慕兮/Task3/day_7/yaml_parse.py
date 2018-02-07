# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

import yaml
# import sys
import codecs

if __name__ == "__main__":
    print("python yaml基础示例")

    document = '''
    公众号: 开源优测
    基本信息:
        创建人: 苦叶子
        id: DeepTest
    '''
    load = yaml.load(document)
    print(type(load))
    print(load)

    print("--"*25)

    output = yaml.dump(load)
    print(type(output))
    print(output)
    '''
    # fp = open("yaml_data.yaml", "r", encoding="utf-8")
    # python给我们提供了一个包codecs进行文件的读取，这个包中的open()
    # 函数可以指定编码的类型：
    fp = codecs.open("yaml_data.yaml", "r", encoding="utf-8")#如果open时使用的encoding
    # 和文件本身的encoding不一致的话，那么这里将将会产生错误
    document = fp.read()
    # document = fp
    fp.close()

    # 将yaml格式内容 转换成 dict类型
    load = yaml.load_all(document)
    print(type(load))

    for data in load:
        print(type(data))
        print(data)

        print("---" * 25)
        # 将python对象转换成为yaml格式文档

        output = yaml.dump(data, encoding = "utf-8")
        print(type(output))
        print(output)

        print("\\u5F00\\u6E90\\u4F18\\u6D4B\\u4FE1\\u606F")
        print("\u5F00\u6E90\u4F18\u6D4B\u4FE1\u606F")

        # print(output.encode("utf-8").decode("unicode_escape"))#'unicode_escape'
'''