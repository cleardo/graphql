# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.configuration.GraphqlQueryLib import *
import unittest
import json


class GetDeployConfig(unittest.TestCase):

    # 测试GetDeployConfig, configurationId正确， SN正确
    def test_get_deploy_config(self):
        PanelList = getRandomPanelSNAndName()
        SN = PanelList[0]['SN']
        configId = getRandomConfigurationIdList()[0]
        r = queryDeployConfiguration(serialNumber=SN, configurationId=configId)
        self.assertEqual(r["data"]["deployConfiguration"], "success")

    # 测试 正确的configurationId 与错误的 SN
    def test_true_configId_errorSN(self):
        SN = getTimeStr("error_sn")
        configId = getRandomConfigurationIdList()[0]
        r = queryDeployConfiguration(serialNumber=SN, configurationId=configId)


if __name__ == '__main__':
    unittest.main()
