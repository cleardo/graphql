# coding=utf-8
# 设置Python文件编码, 注意要有#号,这行是备注,下面那一行不是！


# 导入uniitest库
import unittest

# 导入requests库(前提你已经安装好了)
import requests


# 构造一个类, 继承unittest
class Mytest(unittest.TestCase):

    # 初始化数据(setUp是unittest提供的初始化功能)
    def setUp(self):
        # 设置url
        self.url = "http://freeapi.ipip.net"
        # 设置参数
        self.para = "8.8.8.8"

    # 定义一个方法开始测试, 必须以test开头, 否则Uniitest不识别！
    def test_mytest(self):
        # 由于是get方法, 直接将参数连接到 Url后面

        url = self.url + "/" + self.para
        r = requests.get(url=url)

        # --------------------断言 assert--------------------
        # 断言API正在运行  assertEqual API server is running

        self.assertEqual(r.status_code, 200)
        print r.text


if __name__ == '__main__':
    unittest.main()