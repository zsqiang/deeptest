# _*_ coding : utf-8 _*_
__author__ = "Jason_copy"

'''
遍历某个文件夹下面的所有子文件夹和文件名称

“只有提升维度，不断抽象，才能够看清低维度的事物的本质。”  -  柏拉图-理想国

问题：
    遍历系统某个文件夹下面的所有子文件夹和文件，并打印出来
解决方案：
    获取系统文件的路径，创建一个字典
    列出当前文件夹下的子文件夹和文件，文件夹存储为字典的key1，文件存储为字典的key2
    遍历字典中的每一个文件夹和文件
讨论：
    当文件/文件夹名称为汉字时，没有测试
    如何根据key，快速查找当前key及以该key为父目录的所有子目录和子文件，没有实现
    封装性不好，class和独立函数混合
'''
#from __future__ import print_function
#from __future__ import with_statement
import os
import sys

class traverse_name():
    def __init__(self,path,father_dir):
        self.path = path + father_dir

    def show_name(self):
        '''显示当前路径下的文件夹和文件'''
        print(os.listdir(self.path))
        list0 = os.listdir(self.path)
        print(list0)
        print(os.walk(self.path))

        list_dir = []
        list_file = []

        for i in list0:
            if os.path.isdir(self.path + '\\' + i):
                list_dir.append(i)
            else:
                list_file.append(i)
        return list_dir,list_file

def iter_dir(abs_path,dir_father_path,dir_res):
    #父目录下没有子目录，则返回0
    if 0 == len(dir_res[dir_father_path]['dir']):
        return 0

    for dir in dir_res[dir_father_path]['dir']:
        dir_son_path = dir_father_path + '\\' + dir
        dir_res[dir_son_path] = dict()
        #abs_path为绝对路径，dir_path为相对路径
        traverse = traverse_name(abs_path,dir_son_path)
        dir_res[dir_son_path]['dir'],dir_res[dir_son_path]['file'] = traverse.show_name()
        '''
        #父目录下存在子目录
        if 0 != len(dir_res[dir_son_path]['dir']):
            dir_path = dir_father_path + '\\' + dir_son_path
            for dir_son_path in dir_res[dir_path]['dir']:
                iter_dir(dir_path,dir_son_path,dir_res)
        '''
        iter_dir(abs_path,dir_son_path,dir_res)
def show_res(result):
    print(result)
    list0 = []
    for key in result:
        print(len(key))
        list0.append(len(key),key)
        list0.sort()
        print(list0)
    for i in range(0,len(list0),1):
        key = list0[i][1]
        print('目录：',key)
        print('包含目录：',result[key]['dir'])
        print('包含文件：',result[key]['file'])

if __name__ == "__main__":
    # filename = '1.txt'
    # os.remove(filename)
    # print(os.getcwd())
    # f = open(filename, 'w+')
    # f.writelines('a\n')
    # f.writelines('ab\n')
    # f.writelines('abc\n')
    # f.close()
    # f = open(filename, 'r+')
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # f.close()

    # list = os.listdir(dir)  # 列出目录下的所有文件和目录
    # if os.path.isdir(filepath):  # 如果filepath是目录，则再列出该目录下的所有文件
    # os.path.isfile(path):
    # elif os.path:  # 如果filepath是文件，直接列出文件名
    # os.walk(path),遍历path，返回一个对象，
    # 他的每个部分都是一个三元组,
    # ('目录x'，[目录x下的目录list]，目录x下面的文件)
    # os.path.join(name)
    # path = sys.path[0]

    result = dict()

    abs_path = os.getcwd()
    print(abs_path)
    father_dir = '\A'

    traverse = traverse_name(abs_path,father_dir)
    result[father_dir] = dict()
    result[father_dir]['dir'], result[father_dir]['file'] = traverse.show_name()

    iter_dir(abs_path, father_dir, result)

    show_res(result)