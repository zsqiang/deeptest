#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 19:33:45
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,re,pyperclip,zipfile
import isNum

class backup():
    def __init__(self,path):
        self.path = path

    def filedir(self):
        filename = []
        fileReg = re.compile(r'(.*(.txt|.py))$')
        for root, dirs, files in os.walk(self.path):
            for name in files:
                regF = fileReg.findall(name)
                if regF != []:
                    f = root + '\\' + str(regF[0][0])
                    filename.append(f)
#                    print('文件：{0}'.format(f))
            for name in dirs:
                if root == self.path:
                    d = root + name
                else:
                    d = root + '\\' + name
#                print('目录：{0}'.format(d))
        return filename

    def backup(self):
        f = backup(self.path).filedir()
        os.chdir(self.path)
        newzip = zipfile.ZipFile('abc1.zip','a')
        for i in f:
            newzip.write(i,compress_type=zipfile.ZIP_DEFLATED)
        newzip.close()

if __name__ == '__main__':
    path = 'D:\\github\\deeptest\\第一期\\广州-Roger'
    f = backup(path)
    f.backup()