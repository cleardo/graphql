# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.configuration.GraphqlQueryLib import *
import unittest
import json


class DeleteConfiguration(unittest.TestCase):

    # 删除configuration: 先创建再删除
    def test_delete_configuration(self):

        # 创建configraution 获取confiurationId
        name = getTimeStr('QATester')
        description = "QATester"
        r = queryCreateConfiguration(name, description, showprint=False)
        configurationId = r["data"]["createConfiguration"]["configurationId"]

        # 删除上面创建的configuraiton
        r = queryDeleteConfiguration(configurationId)
        self.assertTrue(r["data"]["deleteConfiguration"]["success"])

    # 删除不存在的configuration
    def test_delete_not_esxit_configraution(self):
        configurationId = getTimeStr()
        r = queryDeleteConfiguration(configurationId)
        self.assertIsNotNone(r["errors"])


if __name__ == '__main__':
    unittest.main()
