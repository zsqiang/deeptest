#coding=utf-8

if __name__ == "__main__":

    str_demo = "  我的前 后 左右都有空格  "

    #去除前面空格
    lstr = str_demo.lstrip()
    print(lstr)

    #去除后面空格
    rstr = str_demo.rstrip()
    print(rstr)

    #去除前后的空格
    str = str_demo.strip()
    print(str)

