# coding=utf-8

"""
全局数据使用的demo
"""

import unittest

global_string = None

__author__ = 'Administrator'


import requests


class GlobalTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_case_1(self):

        globals()['global_string'] = "test_case_1"
        # 断言global_string已经被修改
        self.assertNotEqual(global_string, None)
        proxies = {'http': '192.168.1.115:8888'}
        res = requests.get("http://www.baidu.com", proxies=proxies)
        print(res.encoding)
        print("状态码：")
        print(res.status_code)
        print("response body: ")
        print(res.text)
        print(res)

    def test_case_2(self):
        global global_string
        # 断言global_string的值为test_case_1中修改的值，
        # 即cases间数据共享
        self.assertEqual(global_string, "test_case_1")

if __name__ == "__main__":
    unittest.main()
