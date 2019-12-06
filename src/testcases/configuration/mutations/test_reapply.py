# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.configuration.GraphqlQueryLib import *
import unittest
import json


class Reapply(unittest.TestCase):

    # 测试 reapply 接口
    def test_reapply(self):
        configId = getRandomConfigurationIdList()[0]
        r = queryReapply(configId)
        self.assertEqual(r["data"]["reapply"], "success")

    # 测试错误的configurationId 部署
    def test_error_reapply(self):
        r = queryReapply(getTimeStr('error_configId'))
        self.assertIsNotNone(r["errors"])

    def test_empty_reapply(self):
        r = queryReapply('')
        self.assertIsNotNone(r["errors"])


if __name__ == '__main__':
    unittest.main()
