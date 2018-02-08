import yaml
print("python yaml基本示例")
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

#示例2
import yaml
import codecs
print("python yaml基本示例")
fp = codecs.open("yaml_data.yaml", "r", "utf-8")
document = fp.read()
fp.close()
# 将yaml格式内容 转换成 dict类型
load = yaml.load_all(document)
# 遍历迭代器
for data in load:
    print(type(data))
    print(data)
    print("---" * 25)
    # 将python对象转换成为yaml格式文档
    output = yaml.dump(data)
    print(type(output))
    print(output)


