# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.configuration.GraphqlQueryLib import *
import unittest
import json


class DeployConfiguration(unittest.TestCase):

    # 测试 confiugraiton
    def test_deploy_configuration(self):
        configId = getRandomConfigurationIdList()[0]
        PanelList = getRandomPanelSNAndName()
        SN = PanelList[0]['SN']
        r = queryDeployConfiguration(configurationId=configId, serialNumber=SN)
        self.assertEqual(r['data']['deployConfiguration'], "success")

    """
    测试 serialNumbers 与 configuration 的笛卡尔积
    控制 serialNumbers 正确
    """
    def test_true_serialNumbers(self):
        PanelList = getRandomPanelSNAndName()
        SN = PanelList[0]['SN']

        def true_configurationId():
            configId = getRandomConfigurationIdList()[0]
            r = queryDeployConfiguration(configurationId=configId, serialNumber=SN)
            self.assertEqual(r['data']['deployConfiguration'], "success")

        true_configurationId()

        def error_configurationId():
            r = queryDeployConfiguration(configurationId=getTimeStr('error_configId'), serialNumber=SN)
            self.assertIsNotNone(r["errors"])

        error_configurationId()

        def empty_configurationId():
            r = queryDeployConfiguration(configurationId='', serialNumber=SN)
            self.assertIsNotNone(r["errors"])

        empty_configurationId()

    """
        测试 serialNumbers 与 configuration 的笛卡尔积
        控制 configuration 正确
    """
    def test_true_configurationId(self):
        configId = getRandomConfigurationIdList()[0]

        def error_serialNumbers():
            r = queryDeployConfiguration(configurationId=configId, serialNumber=getTimeStr('error_sn'))
            self.assertIsNotNone(r["errors"])
        error_serialNumbers()

        def empty_serialNumbers():
            r = queryDeployConfiguration(configurationId=configId, serialNumber='')
            self.assertIsNotNone(r["errors"])
        empty_serialNumbers()


if __name__ == '__main__':
    unittest.main()
