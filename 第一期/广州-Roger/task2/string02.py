#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-23 16:17:13
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

import os

str1 = "this is really a string example....wow!!!"
str2 = "is"

print (str1[str1.rfind(str2)+1:])

print (str1[str1.rfind(str2, 0, 10):7])