# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.configuration.GraphqlQueryLib import *
import unittest
import json


class ConfigurationDetail(unittest.TestCase):

    # 测试 configuration-detail 随机获取configurationId
    def test_configuration_detail(self):
        ID = getRandomConfigurationIdList()[0]
        r = queryConfigurationDetail(ID)
        self.assertEqual(r["data"]["configurationDetail"]["configurationId"], ID)

    # 测试 configurationId为空
    def test_configurationId_is_empty(self):
        r = queryConfigurationDetail('')
        self.assertIsNotNone(r["errors"])

    # 测试configurationId为错误值
    def test_configurationId_is_wrong(self):
        r = queryConfigurationDetail(getTimeStr('wrong'))
        self.assertIsNotNone(r["errors"])


if __name__ == '__main__':
    unittest.main()
