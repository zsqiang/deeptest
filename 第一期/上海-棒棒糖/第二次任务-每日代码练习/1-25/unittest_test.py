import unittest
from mydict_test import Dict
class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEqual(d.a,1)  #断言函数返回的结果与1相等
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d=Dict()
        d['key']='value'
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d=Dict()
        d.key='value'
        self.assertTrue('key'in d)
        self.assertEqual(d['key'],'value')
    def test_keyerror(self):
        d=Dit()
        with self.assertRaises(KeyError):  #断言就是期待抛出指定类型的Error,如通过d['empty']访问不存在的key时，断言会抛出KeyError
            value=d['empty']
    def test_attrerror(self):
        d-Dict
        with self.assertRaises(ArithmeticError):  #通过d.empty访问不存在的key时，我们期待抛出AttributeError
            value=d.empty
if __name__ == '__main__':
    unittest.main()



