# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.configuration.GraphqlQueryLib import *
import unittest
import json


class GetAppliedPanel(unittest.TestCase):

    # 先部署，再获取
    def test_get_applied_panel(self):
        PanelList = getRandomPanelSNAndName()
        SN = PanelList[0]['SN']
        configId = getRandomConfigurationIdList()[0]
        queryDeployConfiguration(serialNumber=SN, configurationId=configId, showprint=False)
        r = queryGetDeployConfig(SN)
        self.assertIsNotNone(r["data"]["getDeployConfig"])


if __name__ == '__main__':
    unittest.main()
