#!/usr/bin/env python
# encoding: utf-8
'''
可变长度参数：
在编程的过程中，可能会遇到函数参数个数不固定的情况，这时就需要使用可变长度的函数参数。
在python 函数定义中，使用*和**符号分别指定元祖(非关键字)和字典(关键字)作为参数
非关键字边长参数(元祖)
当函数被调用的时候，所有的参数都将值赋给了在函数声明中对应的局部变量，剩下的非关键字参数按照顺序添加到一个元祖中便于访问
可变长元祖参数必须在文职和默认参数之后，所以使用可变长元祖参数的函数形式如下：(中括号表示可选参数，可变长元祖参数前有一个*符号)
'''
def argFunc(positional_arg,keyword_arg ='foo',*tuple_grp_nonkw_args):
	print 'positional_arg:',positional_arg
	print 'keyword_arg：',keyword_arg
	for arg in tuple_grp_nonkw_args:
		print 'additional_arg:',arg

print argFunc(3)
print argFunc(3,4)
print argFunc(3,4,'hello','world')


'''
关键字变长参数(字典)
可变长字典参数必须是函数定义中的最后一个参数，所以使用可变长字典惨呼的函数形式一般如下(中括号
表示可选参数)，可变长字典参数前有一个**符号
'''
def argFunc(positional_arg,keyword_arg='foo',*tuple_grp_nonkw_args,**dict_grp_kw_args):
	print 'positional_arg：',positional_arg
	print 'keyword_arg:',keyword_arg
	for arg in tuple_grp_nonkw_args:
		print 'additional non-keyword arg:',arg
	for argkey in dict_grp_kw_args.keys():
		print 'additional keyword args:{"%s":"%s"}'%(argkey,dict_grp_kw_args[argkey])

print argFunc(3,4,name='zhangsan',age=28)
print argFunc(3,4,'hello','world',name='lisi',age=28)

'''
函数调用的完整形式为：
func(positional_args,keyword_args,*tuple_grp_nonkw_args,**dict_grp_kw_args)
在使用的过程中，所有参数都是可选的，但是注意的是，上面四种参数的位置是不可调换的
'''