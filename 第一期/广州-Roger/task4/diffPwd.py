#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 19:33:45
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,re,pyperclip
import isNum

class diffpwd():
    def __init__(self):
        pass

    def diff(self,a):
        pwd1Reg = re.compile(r'[a-z]+')
        pwd2Reg = re.compile(r'[A-Z]+')
        pwd3Reg = re.compile(r'[0-9]+')
        if re.search(pwd1Reg,a) == None or re.search(pwd2Reg,a) == None \
                or re.search(pwd3Reg,a)== None or len(a) < 8:
            print("密码需要8个字符以上，包含大小写和数字")
            return None
        else:
            print("密码设置成功")
            return a

if __name__ == '__main__':
    text = str(pyperclip.paste())
    f = diffpwd()
    pwd = f.diff(text)
    print(pwd)