#coding=utf-8

if __name__ == "__main__":

    source_str = "it's my book,please show it"

    #source_str从左到右查找my
    print("从左到右查找my")
    print(source_str.find("my"))
    print(source_str.index("my"))

    #source_str从右到左查找my
    print("从右到左查找my")
    print(source_str.rfind("my"))
    print(source_str.rindex("my"))

    #替换
    print("将my替换成your")
    des_str = source_str.replace("my","your")
    print(des_str)

