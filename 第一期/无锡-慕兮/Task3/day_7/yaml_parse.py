# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

import yaml
import codecs

if __name__ == "__main__":
    print("python yaml基础示例")

    # document = '''
    # 公众号: 开源优测
    # 基本信息:
    #     创建人: 苦叶子
    #     id: DeepTest
    # '''
    # load = yaml.load(document)
    # print(type(load))
    # print(load)
    #
    # print("--"*25)
    #
    # output = yaml.dump(load)
    # print(type(output))
    # print(output)
    fp = codecs.open("yaml_data.yaml", "r", encoding="utf-8")
    document = fp.read()
    fp.close()

    # 将yaml格式内容 转换成 dict类型
    load = yaml.load_all(document)
    print(type(load))

    for data in load:
        print(type(data))
        print(data)

        print("---" * 25)
        # 将python对象转换成为yaml格式文档
        output = yaml.dump(data)
        print(type(output))
        print(output, end="--")
