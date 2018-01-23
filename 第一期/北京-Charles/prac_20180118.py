# -*- coding:utf-8 -*-

if __name__ == '__main__':
    d1 = {'id':1,'sku':'apple','city':'beijing'}
    d2 = {"id":2,'sku':'grape','city':'xiamen'}
    l1=['id','name','school','age']
    print(len(d1))
    print(d2)

    str_d1=str(d1)
    print(type(str_d1))
    print(str_d1)
    # copy复制字典
    d1_cp = d1.copy()
    print(d1_cp)
    # fromkeys创建字典
    dict_new = dict.fromkeys(l1,'v')
    print(dict_new)
    # get获取指定key的value
    v1 = d1.get('sku')
    print(v1)

    # in, 判断key是否存在
    result1 = 'sku' in d1
    print(result1)
    # items,以元组形式返回字典所有的(key, value)
    item = d1.items()
    print(item)
    # keys 以列表形式返回字典所有的key
    key = d1.keys()
    print(key)
    # setdefault, 如果key存在，则返回其对应的value，
    # 否则将该key和默认值插入到字典中，并返回默认值
    set1=d1.setdefault('book','memeda')
    set2=d1.setdefault('city','Harbin')
    print(set2)
    print(d1)
    # update, 更新字典
    d1.update(dict_new)
    print(d1)
    # values,以列表形式返回字典中所有的value
    values = d1.values()
    print(values)

    ##遍历、修改、删除
    # 遍历 方法1
    for (key,value) in d2.items():
        print("%s : %s" % (key, value))
    # 遍历 方法2
    for key in d2.keys():
        print('%s : %s'%(key,d2[key]))

    #修改
    d2['sku']='woaihuiying'
    print(d2['sku'])

    # 删除指定元素,删除key即可
    del d2['sku']
    print(d2)

    ## 清空字典
    d2.clear()
    print(d2)

    #set
    print(u"set操作示例")
    set_source = set([1, 1, 2, 3, 4, 5, 6, 7])
    set_demo = set([1, 1, 2, 3, 4, 5, 6, 7])
    print("原始数据： ", end="")
    print(set_source)
    set_source.add(111)
    print(set_source)