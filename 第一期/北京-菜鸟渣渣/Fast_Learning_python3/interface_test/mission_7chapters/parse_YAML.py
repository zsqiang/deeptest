#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")


'''
什么是YAML

YAML参考了其他多种语言，包括：XML、C语言、Python、Perl以及电子邮件格式RFC2822。 Clark Evans在2001年5月在首次发表了这种语言，另外Ingy döt Net与Oren Ben-Kiki也是这语言的共同设计者。

YAML是"YAML Ain't a Markup Language"（YAML不是一种置标语言）的递归缩写。 在开发的这种语言时，YAML 的意思其实是："Yet Another Markup Language"（仍是一种置标语言），

格式及示例

数据结构可以用类似大纲的缩排方式呈现，结构通过缩进来表示，连续的项目通过减号“-”来表示，map结构里面的key/value对用冒号“:”来分隔。

示例如下：

开源优测信息:
    Yoto公众号:
        公众号: OVDeepTest
        中文名: 松青优测
        创建者: 叶子大师
        内容系列:            
            - 接口测试            
            - jmeter            
            - selenium            
            - 快学python3            
            - 大数据测试            
            - 杂谈系列
    web站点:
        中文名: 开源优测社区
        状态: 已暂停
        城市: 广州
        网址: www.testingunion.com


字符串不一定要用双引号标识
在缩排中空白字符的数目并不是非常重要，只要相同阶层的元素左侧对齐就可以了（不过不能使用TAB字符）
允许在文件中加入选择性的空行，以增加可读性
在一个档案中，可同时包含多个文件，并用“——”分隔
选择性的符号“...”可以用来表示档案结尾（在利用串流的通讯中，这非常有用，可以在不关闭串流的情况下，发送结束讯号）
'''

import  yaml
import  codecs

import  codecs, sys

if __name__ != '__main__':
    document = """
       公众号: 开源优测
       基本信息:
           创建人: 苦叶子
           id: DeepTest
       """

    # 将yaml格式内容 转换成 dict类型
    load = yaml.load(document)
    print(type(load))
    print(load)

    print("---" * 25)

    # 将python对象转换成为yaml格式文档
    output = yaml.dump(load)
    print(type(output))
    print(output)


if __name__ == '__main__':
    fp=codecs.open("yaml_data.yaml","r","utf-8")
    document=fp.read()
    fp.close()

    ## 将yaml格式内容 转换成 dict类型
    load=yaml.load_all(document)

    for data in load:
        logging.info((type(data),data))
        logging.info(type(data),data)
        logging.info("*"*25)
        # 将python对象转换成为yaml格式文档
        output=yaml.dump(data)
        logging.info((type(output), output))





