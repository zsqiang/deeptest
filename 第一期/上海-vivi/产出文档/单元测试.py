测试工具：
1、unittest  -->单元测试
2、doctest   -->文档测试




##单元测试语法结构：

import unittest

class Test**(unittest.TestCase):
	def setUp(self):
		print('setUp....)

	def test_1(self):
		pass
		self.assertEqual(a, b)
		
	def test_2(self):
		pass
		self.assertEqual(c, d)
		
	def tearDown(self): 
		print('tearDown)

if __name__ == '__main__':
	unittest.main()
	
结构说明：
1. 类的命名开头要大写，最好Test,继承unittest.TestCase；
2. setUp和tearDown初始化，在每调用一个方法的前后分别被执行。相当于setUP-->test_1-->tearDown,setUp -->test_2 -->tearDown
3.unittest.main()实例化	
	
	
	
###文档测试
