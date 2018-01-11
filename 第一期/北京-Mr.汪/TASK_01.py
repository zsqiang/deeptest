#! -*- coding:utf-8 -*-

# author 改为你的

__author__ == "Mr.汪"

import json
import requests
import unittest

class weatherApiTest(unittest.TestCase):
    """
    测试用例
    """
    def setUp(self):
        print("start")

    def test_weatherApi(self):
        """
        执行用例是否与期望相同
        """
        url = "http://wthrcdn.etouch.cn/weather_mini"

        params = {
            "city":"北京"
        }

        result = requests.get(url,params = params)
        result = json.loads(result.text)
        cutresult = result["data"]["forecast"][0]["type"]
        print(cutresult)
        if (cutresult == "晴"):
            print("验证通过")
        else:
            print("验证失败")

    def tearDown(self):

        pass

if __name__ == '__main__':
    """
    主函数入口
    """
    unittest.main(verbosity=2)


