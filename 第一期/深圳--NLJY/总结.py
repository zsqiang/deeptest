# import os
# print("获取当前工作目录")
# print(os.getcwd())  # 返回的是当前工作的目录
# print(os.curdir)
# os.mkdir('test_mk11')    # 创建目录，这个目录必须是不存在的。否则抛出异常
# os.rename('test_mk11','test_mk22') # 重命名目录，子文件
# print("改变工作目录到dirname")
# os.chdir('f:')
# print(os.getcwd())
# # path模块常用方法
import json
print('json转dict')
json_str ='{'name':'开源优测','url':'www.testingunion.com','id':'deeptest'}'
print('原类型:',type(json_str))
