# -*- coding:utf-8 -*-

__author__ = 'catleer'

import os

# os模块的目录操作方法
def opreate_catelog():
    # 返回完整的路径目录
    print("获取当前工作目录")
    print(os.getcwd())

    # 返回“.“
    print("获取当前目录")
    print(os.curdir)

    # 创建一个不存在的目录
    # os.mkdir("G:\\test_mk1")

    # 重命名目录
    # os.rename("G:\\test_mk1", "G:\\test_mk2")

    # 删除指定目录：目录应该为空文件夹且目录必须存在
    os.removedirs("G:\\test_mk2")

    # 改变工作目录到G盘
    print("改变工作目录到dirname")
    os.chdir("G:")
    print(os.getcwd())

# path模块操作文件，对文件进行管理
def opreate_file():
    # 先初始化当前文件全路径变量
    path = __file__
    print("当前文件全路径为：%s" % path)

    # 是目录则返回true,否则返回false
    print("目录判断：%s" % os.path.isdir(path))

    # 判断是否为文件，是则返回True，否则返回false
    print("文件判断： %s" % os.path.isfile(path))

    # 判断目录或文件是否存在
    print("目录/文件存在： %s" % os.path.exists(path))

    # 判断文件大小，若路径为目录，则返回0
    print("文件大小：%s" % os.path.getsize(path))

    # 获取文件的绝对路径
    print("文件绝对路径：%s" % os.path.abspath(path))

    # 将目标路径规范化
    print("规范化路径：%s" % os.path.normpath(path))

    # 将文件名和目录分割
    # 若传入的是目录，则将最后的目录名作为文件名分割
    print("目录和文件名分割：", end="")
    print(os.path.split(path))

    # 分离文件名和扩展名
    print("文件名和扩展名分离：", end="")
    print(os.path.splitext(path))

    # 获取文件名
    print("文件名为：%s" % os.path.basename(path))

    # 获取文件所在目录
    print("文件目录为：%s" % os.path.dirname(path))

# 目录遍历方法
def walk_dir(target_dir):
    # root:当前根目录
    # dirs：root下的子目录
    # files：root下的子文件

    walk_result = os.walk(target_dir)

    for root, dirs, files in walk_result:
        print(type(root), type(dirs), type(files))
        print("-", root)

        # 遍历当前子目录
        for name in dirs:
            print(" --", name)

        # 遍历当前目录的子文件
        for name in files:
            print(" --", name)


# opreate_catelog()
# opreate_file()

target_dir = "G:\\"
walk_dir(target_dir)