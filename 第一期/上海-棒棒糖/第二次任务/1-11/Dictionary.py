if __name__=="__main__":
    dict ={'test':'开源优测','book':'python3'}
    print(dict)
    print(len(dict))
    #将字典转换成字符串
    str_d=str(dict)
    print(str_d)
    print(dict)
    #判断类型
    print(type(str_d))
    print(type(dict))


if __name__=='__main__':
    print('字典方法应用示例')
    dict_demo= {'test': '开源优测', 'book': 'python3'}
    tup1=[1,2,3,4]
    #复制字典
    dict_cp=dict_demo.copy()
    print(dict_cp)

    #fromkeys以序列作为kye创建一个新字典，value为所有键对应的初始值
    dict_new=dict.fromkeys(tup1,'value')
    print(dict_new)
    #get获取指定key的value,key不存在，可以返回None，或者自己指定的value
    value1 = dict_demo.get("test")
    value2 = dict_demo.get("python3")
    value3 = dict_demo.get("book",'自己指定的value')
    print(value1)
    print(value2)
    print(value3)
    #in, 判断key是否存在,存在返回true
    key="book"
    result1=key in dict_demo
    result2=key in dict_new
    print(result1)
    print(result2)
    ## items, 以列表包含元组形式返回字典所有的(key, value)，用于遍历
    items=dict_demo.items()
    print(items)

   #.keys() 以列表形式返回字典所有的key
    dict_demo_keys=dict_demo.keys()
    print(dict_demo_keys)
    #.values()以列表形式返回字典所有的value
    dict_demo_values = dict_demo.values()
    print(dict_demo_values)

    # setdefault, 如果key存在，则返回其对应的value，
    # 否则将该key和默认值插入到字典中，并返回默认值
    dict_demo = {'test': '开源优测', 'book': 'python3'}
    set_result1 = dict_demo.setdefault('test', '指环王')
    set_result2 = dict_demo.setdefault('我是key', '插入这个值')
    print(set_result1)
    print(set_result2)
    print(dict_demo)
    # update 更新字典 将两个字典合并
    dict_demo.update(dict_new)
    print(dict_demo)
    #有就修改，没有就新增
    dict_demo2 = {'test': '开源优测', 'book': 'python3'}
    dict_demo2['test']='指环王2'
    dict_demo2['我是key1'] = '插入这个值1'
    print(dict_demo2)

    # 删除指定元素
    del dict_demo2["book"]
    print(dict_demo2)

    # 清空字典
    dict_demo2.clear()
    print(dict_demo2)
