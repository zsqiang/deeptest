#coding=utf-8


if __name__ == "__main__":
    
    set_source = set([1,2,3,3,1,8,4])
    list_demo = ["a","b","c"]

    print("打印原始集合")
    print(set_source)

    print("set_source新增元素9后")
    set_source.add(9)
    print(set_source)

    print("set_source删除元素1后")
    set_source.remove(1)
    print(set_source)

    print("新增多个元素后")
    set_source.update(list_demo)
    print(set_source)
