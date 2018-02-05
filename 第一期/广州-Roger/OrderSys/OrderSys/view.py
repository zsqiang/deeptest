#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29 20:27:15
# @Author  : Roger TX (425144880@qq.com)
# @Link    : https://github.com/paotong999
# @Version : $Id$

from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! ")
