#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 19:33:45
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,re,pyperclip,zipfile
import isNum

class removeBig():
    def __init__(self,path):
        self.path = path

    def filedir(self):
        l = []
        i = 0
        for root, dirs, files in os.walk(self.path):
            for name in files:
                i = i + 1
                f = root + '\\' + name
                g = os.path.getsize(f)
                if g < 1024:
                    l.append(f)
                    print('{2}、{0}文件大小为：{1}b'.format(f,g,i))
                elif g < 1024 * 1024:
                    g = g / 1024
                    l.append(f)
                    print('{2}、{0}文件大小为：{1:.2f}kb'.format(f,g,i))
                else:
                    g = g / (1024 * 1024)
                    l.append(f)
                    print('{2}、{0}文件大小为：{1:.2f}mb'.format(f,g,i))
        return l

    def remove(self):
        f = removeBig(self.path).filedir()
        x = int(input('请输入要删除的文件序号：'))
        os.unlink(f[x-1])

if __name__ == '__main__':
    path = 'D:\\github\\deeptest\\第一期\\广州-Roger\\task1'
    f = removeBig(path)
    f.remove()