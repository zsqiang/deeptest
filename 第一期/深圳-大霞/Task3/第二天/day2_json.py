"""
json解析
JSON 语法规则：在javascript语言中，一切都是对象。因此，任何支持的类型都可以通过json来表示，例如字符串、数字、对象、数组等。
但是对象和数组是比较特殊且常用的两种类型：
对象表示为键值对
数据由逗号分隔
花括号保存对象
方括号保存数组
"""
# python json解析模块
# 第一步，导入json模块
import json
"""
python json解析常用函数：
json.dumps:将python对象编码成json字符串
json.loads:将已编码的json字符串解码为pthon对象
"""
class jjson:
    #封装一个json函数，解析通用类
    def json_read(self,file):
        fp=open(file,'r')
        json_data=json.load(fp)
        print(json_data)
        fp.close()
    def json_writer(self,file,writer_data):
        fp=open(file,'w')
        json.dump(writer_data, fp, sort_keys=True, indent=4, separators=(',', ':'))
        fp.close()

if __name__=="__main__":
    print("将python对象转换成json对象")
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    json_data=json.dumps(data)#将python对象编码成json字符串
    print("python对象类型：%s"% type(data))
    print("json对象类型：%s"%type(json_data))
    print(" ")


    #将json转换成python对象
    python_data=json.loads(json_data)
    print(type(json_data))
    print(type(python_data))
    print(python_data)

    print("python json串格式化实例")
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    json_data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

    # 打印格式化的json串
    print(json_data)

    print("python 读取json内容文件转化python对象实例")
    # fp = open('D:/json_read.json', 'r')
    # json_data=json.load(fp)
    # print(type(json_data))
    # print(json_data)
    # fp.close()
    #
    # print("python 写json串实例")
    # data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    # fp=open('D:/json_write.json','w')
    # # 以可读性格式写入json_write.json文件中
    # json.dump(data, fp, sort_keys=True, indent=4, separators=(',', ': '))
    # fp.close()
    print("读取json文件为python实例对象")
    jsData=jjson()
    f='D:/json_read.json'
    jsData.json_read(f)
    print("写入json文件实例")
    write_data = [{'a': 223, 'b': 22, 'c': 22, 'd': 22, 'e': 22}]
    ff='D:/json_write.json'
    jsData.json_writer(ff,write_data)

