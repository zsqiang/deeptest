#coding=utf-8

if __name__ == "__main__":

    dict = {"test01":"01","test02":"02","test03":"03"}
    tupl1 = [1,2,3,4,5]

    print("打印字典的长度")
    print(len(dict))

    print("将字典转换为字符串")
    str_d = str(dict)
    print(str_d)
    print(type(str_d))

    print("创建字典")
    dict_new = dict.fromkeys(tupl1,"value")
    print(dict_new)

    print("获取key test01的value值")
    print(dict.setdefault("test01"))

    print("更新字典")
    dict.update(dict_new)
    print(dict)

    print("返回字典中所有的value")
    values = dict.values()
    print(values)