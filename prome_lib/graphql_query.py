# coding=utf-8
# 设置Python文件编码, 注意要有#号,这行是备注,上面面那已行不是！而且编码信息必须写在第一行！


# 导入uniitest库
import unittest

# 导入requests库(前提你已经安装好了)
import requests

# 导入json库(前提你已经安装好了)
import json


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
        # 由于是get方法, 直接将参数连接到 Url后面, python连接字符串就是这么简单！
        url = self.url + "/" + self.para

        # 使用requests发送请求, 返回的是respons对象, 不是字符串！
        r = requests.get(url=url)

        # 将返回的结果转为文本
        r_text = r.text

        # 将文本转为Json, 为什么转为json？ 因为文本是没有数据结构的！
        # 而json可以存放各种类型的数据结构
        r_json = json.loads(r_text)

        # 进行断言, 什么是断言？ 断言就是判断！
        self.assertEqual(r.status_code, 200)  # 这个断言返回的状态码是200

        # 从postman测试中我知道他会返回数组,所以使用数组索引,
        self.assertEqual(r_json[0], "GOOGLE.COM")

        # 打印结果
        print r_json


if __name__ == '__main__':
    unittest.main()