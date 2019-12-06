# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.configuration.GraphqlQueryLib import *
import unittest
import json


class UpdateConfiguration(unittest.TestCase):

    # 测试 UpdateConfiguration 接口
    def test_update_configuration(self):
        configId = getRandomConfigurationIdList()[0]
        description = "QATester"
        newName = getTimeStr('QATester-updateConfiguration')
        queryUpdateConfiguration(configurationId=configId, description=description, name=newName)

    # 测试错误的configuration
    def test_error_configId(self):
        queryUpdateConfiguration(configurationId=getTimeStr('error-configId'), description="QATester",
                                 name='newName')

    """
    测试 configurationId 与 name 之间的笛卡尔积
    控制 configurationId 正确
    """
    def test_true_configurationId(self):
        configId = getRandomConfigurationIdList()[0]
        description = "QATester"

        def existed_name():
            name = queryConfigurationDetail(getRandomConfigurationIdList()[0],
                                            showprint=False)["data"]["configurationDetail"]["name"]
            r = queryUpdateConfiguration(configurationId=configId, description=description, name=name)
            self.assertEqual(r["data"]["updateConfiguration"]["configurationId"], configId)
            self.assertEqual(r["data"]["updateConfiguration"]["name"], name)

        existed_name()

        def empty_name():
            r = queryUpdateConfiguration(configurationId=configId, description="QATester", name='')
            self.assertIsNotNone(r["errors"])

        empty_name()


if __name__ == '__main__':
    unittest.main()
