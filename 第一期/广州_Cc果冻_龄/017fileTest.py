#coding=utf-8

from __future__ import print_function
import os

if __name__ == "__main__":

    print("获取当前工作目录")
    print(os.getcwd())

    print("获取当前目录")
    print(os.curdir)

    #创建一个目录
    os.mkdir("test01")

    #重命名
    os.rename("test01","test02")

    #删除目录
    os.removedirs("test02")

    print("改变工作目录")
    os.chdir("f:")
    print(os.getcwd())