# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.configuration.GraphqlQueryLib import *
import unittest
import json


class ConfigurationList(unittest.TestCase):

    # 测试获取configuration列表
    def test_queryConfigurationList(self):

        r = queryConfigurationList(pageNumber=10, pageSize=10)
        self.assertIsNotNone(r["data"]["configurationList"])

    """
    测试pageNumber与pageSize的笛卡尔积
    控制pageNumber变量
    """

    # 测试 pageNumber=5条件下的笛卡尔积
    def test_pageNumber_eq5(self):
        pageNumber = 5

        # 测试 pageSize=5
        def pageSize_eq5():
            r = queryConfigurationList(pageNumber, pageSize=5)
            self.assertIsNotNone(r["data"]["configurationList"])
        pageSize_eq5()

        # 测试 pageSize=0
        def pageSize_eq0():
            r = queryConfigurationList(pageNumber, pageSize=0)
            self.assertIsNotNone(r["data"]["configurationList"])
        pageSize_eq0()

        # 测试 pageSize=-1
        def pageSize_plu1():
            r = queryConfigurationList(pageNumber, pageSize=-1)
            self.assertIsNotNone(r["errors"])
        pageSize_plu1()

    # 测试 pageNumber=0条件下的笛卡尔积
    def test_pageNumber_eq0(self):
        pageNumber = 0

        # 测试 pageSize=5
        def pageSize_eq5():
            r = queryConfigurationList(pageNumber, pageSize=5)
            self.assertEqual(len(r["data"]["configurationList"]["configurations"]), 5)
        pageSize_eq5()

        # 测试 pageSize=0
        def pageSize_eq0():
            r = queryConfigurationList(pageNumber, pageSize=0)
            self.assertEqual(len(r["data"]["configurationList"]["configurations"]), 0)
        # pageSize_eq0()

        # 测试 pageSize=-1
        def pageSize_plu1():
            r = queryConfigurationList(pageNumber, pageSize=-1)
            self.assertIsNotNone(r["errors"])
        # pageSize_plu1()

    # 测试 pageNumber=-5条件下的笛卡尔积
    def test_pageNumber_plu5(self):
        pageNumber = -5

        # 测试 pageSize=5
        def pageSize_eq5():
            r = queryConfigurationList(pageNumber, pageSize=5)
            self.assertIsNotNone(r["errors"])
        pageSize_eq5()

        # 测试 pageSize=0
        def pageSize_eq0():
            r = queryConfigurationList(pageNumber, pageSize=0)
            self.assertIsNotNone(r["errors"])
        pageSize_eq0()

        # 测试 pageSize=-1
        def pageSize_plu1():
            r = queryConfigurationList(pageNumber, pageSize=-1)
            self.assertIsNotNone(r["errors"])
        pageSize_plu1()

    """
    测试pageNumber与pageSize的笛卡尔积
    控制pageSize变量
    """

    # 测试 pageSize=5条件下的笛卡尔积
    def test_pageSize_eq5(self):
        pageSize = 5

        # 测试 pageNumber=5
        def pageNumber_eq5():
            r = queryConfigurationList(pageNumber=5, pageSize=pageSize)
            self.assertEqual(len(r["data"]["configurationList"]["configurations"]), pageSize)
        pageNumber_eq5()

        # 测试 pageNumber=0
        def pageNumber_eq0():
            r = queryConfigurationList(pageNumber=0, pageSize=pageSize)
            self.assertEqual(len(r["data"]["configurationList"]["configurations"]), pageSize)
        pageNumber_eq0()

        # 测试 pageNumber=-1
        def pageNumber_plu1():
            r = queryConfigurationList(pageNumber=-1, pageSize=pageSize)
            self.assertIsNotNone(r["errors"])
        pageNumber_plu1()

    # 测试 pageSize=0条件下的笛卡尔积
    def test_pageSize_eq0(self):
        pageSize = 0

        # 测试 pageNumber=5
        def pageNumber_eq5():
            r = queryConfigurationList(pageNumber=5, pageSize=pageSize)
            self.assertEqual(len(r["data"]["configurationList"]["configurations"]), pageSize)
        pageNumber_eq5()

        # 测试 pageNumber=0
        def pageNumber_eq0():
            r = queryConfigurationList(pageNumber=0, pageSize=pageSize)
            self.assertEqual(len(r["data"]["configurationList"]["configurations"]), pageSize)
        pageNumber_eq0()

        # 测试 pageNumber=-1
        def pageNumber_plu1():
            r = queryConfigurationList(pageNumber=-1, pageSize=pageSize)
            self.assertIsNotNone(r["errors"])
        pageNumber_plu1()

    # 测试 pageSize=-5条件下的笛卡尔积
    def test_pageSize_plu5(self):
        pageSize = -5

        # 测试 pageNumber=5
        def pageNumber_eq5():
            r = queryConfigurationList(pageNumber=5, pageSize=pageSize)
            self.assertIsNotNone(r["errors"])
        pageNumber_eq5()

        # 测试 pageNumber=0
        def pageNumber_eq0():
            r = queryConfigurationList(pageNumber=0, pageSize=pageSize)
            self.assertIsNotNone(r["errors"])
        pageNumber_eq0()

        # 测试 pageNumber=-1
        def pageNumber_plu1():
            r = queryConfigurationList(pageNumber=-1, pageSize=pageSize)
            self.assertIsNotNone(r["errors"])
        pageNumber_plu1()


if __name__ == '__main__':
    unittest.main()
