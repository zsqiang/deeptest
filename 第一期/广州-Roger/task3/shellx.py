#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-25 16:38:43
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os,math


cmd = 'sautil{0}{1}'

for i in range(10):
        var = str(i).zfill(4)
        os.system(cmd.format(var,var))
