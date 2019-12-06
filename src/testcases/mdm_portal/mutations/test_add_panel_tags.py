# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json


class AddPanelTags(unittest.TestCase):

    # 测试 随机挑选一个SN加入"QATester"下的一个tag
    def test_add_panel_tags(self):
        PanelList = getRandomPanelSNAndName()
        SN = PanelList[0]['SN']
        tagid = getRandomTagidList()[0]
        r = queryAddpanelTags(serialNumber=SN, tagId=tagid)
        self.assertEquals(r['data']['addPanelTags'], 'success')

    """
    测试 tagid和SN的笛卡尔积
    控制tagid为正确
    """

    def test_add_true_panel_tags(self):
        tagid = getRandomTagidList()[0]

        def error_SN():
            r = queryAddpanelTags(serialNumber=getTimeStr('errortagid'), tagId=tagid)
            self.assertIsNotNone(r["errors"])

        error_SN()

        def true_SN():
            PanelList = getRandomPanelSNAndName()
            SN = PanelList[0]['SN']
            r = queryAddpanelTags(serialNumber=SN, tagId=tagid)
            self.assertEqual(r['data']['addPanelTags'], 'success')

        true_SN()

    """
        测试 tagid和SN的笛卡尔积
        控制SN为正确
    """

    def test_true_SN(self):
        PanelList = getRandomPanelSNAndName()
        SN = PanelList[0]['SN']

        def error_tagid():
            r = queryAddpanelTags(serialNumber=SN, tagId=getTimeStr('errortagid'))
            self.assertIsNotNone(r["errors"])

        error_tagid()
