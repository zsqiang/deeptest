"""
字典dictionary
Dictionnary（字典）是Python最常用的数据类型，它使用方括号{}来标识，其元素为key-value对应，key与value用冒号:分割开
dict = {"key1": "value1", "key2": "value2"}
或是这样创建：
dict = {12: "deeptest", "weixin": "开源优测"}
"""
"""
python中的内置函数：
len
用于计算字典元素的个数, 即key的总数
str
输出字典，即以可打印的字符串输出字典
type
返回变量的类型
"""
if __name__=="__main__":
    print("Dictionary字典实例")
    dict={"Deeptest":"开源优测","book":"快学python"}
    #计算字典的长度
    dict_len=len(dict)
    print("字典的长度：",dict_len)
    #以字符串的方式输出字典
    dict_str=str(dict)
    print("返回字典的字符串形式：",dict_str)
    print(dict)
    #返回转换字符串形式前后数据类型
    print(type(dict_str))
    print(type(dict))
    """
    字典方法：
    clear
    清空字典
    copy
    复制字典
    fromkeys
    以序列作为kye创建一个新字典，value为所有键对应的初始值
    get
    返回指定key的value，如果key不存在，则返回默认值
    in
    判断key是否存在，是则返回True，否则返回False
    items
    返回可遍历的的元组，元组的元素为(key,value)形式
    keys
    返回字典的所有key
    setdefault
    如果key存在，则返回其对应的value，否则将该key和默认值插入到字典中，并返回默认值
    update
    更新字典
    values
    返回字典的所有value值
    """
    dict_demo = {"Deeptest": "开源优测", "book": "快学python"}
    tupl=(1,2,3,4)
    #复制字典
    dict_cp=dict_demo.copy()
    print("打印复制后的字典：",dict_cp)
    #以序列创建一个新的字典
    dict_new=dict_demo.fromkeys(tupl,"value")
    print(dict_new)
    #get获取指定的key对应的value值
    value1=dict_demo.get("Deeptest","我是默认值")
    print(value1)
    value2=dict_demo.get("book")
    print(value2)
    #in,判断key是否存在
    key="Deeptest"
    result1=key in dict_demo
    result2=key in dict_new
    print(result1)
    print(result2)
    #items,以字典形式返回所有的（key,value）
    items=dict_demo.items()
    print(items)
    # setdefault, 如果key存在，则返回其对应的value，
    # 否则将该key和默认值插入到字典中，并返回默认值
    set_resutlt1=dict_demo.setdefault("Deeptest","设置值")
    set_resutlt2=dict_demo.setdefault("我是key","我是value")
    print("返回默认值：",set_resutlt1)
    print("返回设置值：",set_resutlt2)
    print("dict_demo:",dict_demo)
    print("dict_new:",dict_new)
    #更新字典,返回更新后的并集
    dict_demo.update(dict_new)
    print(dict_demo)
    #返回字典的所有value
    values=dict_demo.values()
    print(values)
    """
    字典的value可以存储任何类型Python对象，即可以是标准的类型，也可以是我们自定义的类型，但key不可以。
    字典的key是唯一的，不可以重复
    字典的key可以是数字、字符串甚至元组，但不可以用列表
    """
    #字典遍历、修改、删除
    dict_demo1 = {"DeepTest": "开源优测", "ebook": u"快学Python3"}
    #字典遍历 方法1
    for (key,value) in dict_demo1.items():
        print("%s:%s"% (key,value))
    #字典遍历 方法2
    for key in dict_demo1.keys():
        print("%s:%s" % (key, dict_demo1[key]))
    #修改
    dict_demo1["ebook"]="修改后的值"
    print(dict_demo1)
    #清空字典
    dict_demo1.clear()
    print(dict_demo1)