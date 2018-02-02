import json
'''
if __name__ == "__main__":
    print("python json标准库解析实例")
    data=[{'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}]
    json_data=json.dumps(data)
    # 打印出来看下效果
    print("转化前")
    print(type(data))
    print(data)
    print("-" * 40)
    print("转化后")
    print(type(json_data))
    print(json_data)
    # 将json对象转化成python对象
    print()
    print("将json对象转化成python对象")
    python_data = json.loads(json_data)
    print(type(python_data))
    print(python_data)

    #格式化输出json
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    json_data=json.dumps(data,sort_keys=True,indent=4,separators=(',',':'))
    # 打印格式化的json串
    print(json_data)

    fp=open('json_data.json','r')
    json_data1=json.load(fp)#load()方法从json文件中读取字符串并反序列化
    print(type(json_data1))
    print(json_data1)
    fp.close()

json_data2 = json.loads(fp)#loads()方法把json格式一样的str反序列化
print(type(json_data2))
print(json_data2)


data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
fp=open('json_write.json','w')
# 以可读性格式写入json_write.json文件中
json.dump(data,fp,sort_keys=True,indent=4,separators=(',',':'))
fp.close()

'''
#封装一个json解析通用类
class json_data():
    def json_read(self,file):
        fp = open(file, 'r')
        read_data = json.load(fp)
        print(read_data)
        fp.close()

    def json_writer(self,file,write_data):
        fp = open(file, 'w')
        json.dump(write_data, fp, sort_keys=True, indent=4, separators=(',', ':'))
        fp.close()

file=json_data()
file.json_read('json_data.json')

write_data=[{'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2}]
file.json_writer('json_write.json',write_data)