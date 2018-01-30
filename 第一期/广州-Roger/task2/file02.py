#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-23 16:31:50
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os
'''
用户输入"xxx.txt"类文档文件名
用户输入被替换的"待替换字"
用户输入替换目标"新的字"
用户判断是否全部替换 yes/no
'''

def file_replace(file_name, rep_word, new_word):
    f_read = open(file_name)

    content = []
    count = 0

    for eachline in f_read:
        if rep_word in eachline:
            count = count+eachline.count(rep_word)
            eachline = eachline.replace(rep_word, new_word)
        content.append(eachline)    

    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【Y/N】：' \
                   % (file_name, count, rep_word, rep_word, new_word))

    if decide in ['Y', 'y']:
        f_write = open(file_name, 'w')
        f_write.writelines(content)
        f_write.close()

    f_read.close()


file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name, rep_word, new_word)