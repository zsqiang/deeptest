#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-30 09:25:49
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,sys,pyperclip

password = {'email':'123456',
                      'blog':'1qazXSW@',
                      'centos':'centos',
                      'card':'66666'}

if len(sys.argv) < 2:
    print ('Usage:python password.py [account] - copy account password')
    sys.exit()
    pass

account = sys.argv[1]

if account in password:
    pyperclip.copy(password[account])
    print('password for ' + account + ' copied to clipboard.')
else:
    print('there is no account named ' + account)
    pass
