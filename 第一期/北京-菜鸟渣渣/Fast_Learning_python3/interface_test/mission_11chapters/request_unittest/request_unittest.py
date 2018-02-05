#coding=utf-8

import logging
'''
测试接口

你可以从以下链接获取到我们实例中用到的接口:

http://jsonplaceholder.typicode.com
注意: 因该服务在海外，请勿持续请求该服务的接口。

如果你有需要可以下载对应的服务包，部署到本地来进行测试。

'''
logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")
import requests
import unittest


## 测试用例
class JsonPlaceTest(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.url = "http://jsonplaceholder.typicode.com"
        self.session = requests.session()

        # 测试获取所有用户信息接口

    def test_get_posts(self):
        r = self.session.get(self.url + "/posts")

        print(r.text)

        # 断言状态码
        self.assertEqual(r.status_code, 200)

        # 断言响应头信息
        self.assertEqual(r.headers["Content-Type"],
                         "application/json; charset=utf-8")

        # 断言用户总数
        self.assertEqual(len(r.json()), 100)

        # 测试获取指定用户信息接口

    def test_get_posts_by_id(self):
        r = self.session.get(self.url + "/posts/1")

        # 断言状态码
        self.assertEqual(r.status_code, 200)

        # 断言响应头信息
        self.assertEqual(r.headers["Content-Type"],
                         "application/json; charset=utf-8")

        # 验证用户id
        data = r.json()
        self.assertEqual(data["userId"], 1)

        # 测试删除指定用户信息接口

    def test_delete_posts_by_id(self):
        r = self.session.delete(self.url + "/posts/1")

        # 断言状态码
        self.assertEqual(r.status_code, 200)

        # 断言响应头信息
        self.assertEqual(r.headers["Content-Type"],
                         "application/json; charset=utf-8")

        # 清理

    def tearDown(self):
        if self.session:
            self.session.close()


if __name__ == "__main__":
    print("requests unittest接口测试实例")

    unittest.main()