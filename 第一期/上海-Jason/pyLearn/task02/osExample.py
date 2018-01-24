# _*_ coding : utf-8 _*_
__author__ = "Jason"

import os

if __name__ == "__main__":
    #返回完整的目录路径
    print("获取当前工作目录路径")
    print(os.getcwd())

    #返回的是：.
    print("获取当前目录")
    print(os.curdir)

    #创建目录
    #目标创建目录必须是不存在的，否则抛出异常
    os.mkdir("test_new1")
    os.mkdir("test_mk1")

    #重命名目录
    os.rename("test_new1","test_new2")
    os.renames("test_mk1","test_mk2")

    #删除指定目录
    #要注意目标删除目录必须是无子目录、子文件，即空目录
    #目标删除目录必须存在，否则抛出异常
    #使用该代码时，请将目标删除目录改为你要删除的目录
    #os.removedirs("test_mk11")#[WinError 2] 系统找不到指定的文件。: 'test_mk11'

    #os.removedirs("test_new11")
    #os.removedirs("test_new2")

