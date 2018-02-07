#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-31 09:40:59
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,pyperclip,re

phoneReg = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                        # area code
    (\s|-|\.)?                                # sep
    (\d{3,4})                                # first 3
    (\s|-|\.)?                                # sep
    (\d{4})                                   # last 4
    (\s*(ext|x|ext.)\s*(\d{2,5}))?            # ext
    )''',re.VERBOSE)

emailReg = re.compile(r'''(
    [a-zA-Z0-9.+-]+                     #user
    @                                   #@
    [a-zA-Z0-9.+-]+                     #domain
    \.[a-zA-Z]{2,4}                   #dot
    )''',re.VERBOSE)

c = emailReg.findall('13812345678,13578945623')
text = str(pyperclip.paste())
matches = []

for groups in phoneReg.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum = phoneNum + ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailReg.findall(text):
    print(groups)
    matches.append(groups)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('no phone or email found')
