# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json


class UpdatePanelTags(unittest.TestCase):

    # 测试test_update_panel_tags 接口，tagid为QATester下的一个tag
    def test_update_panel_tags(self):
        tagGroup = "QATester-UpdatePanelTags"
        tagid = getRandomTagidList()[0]
        newName = getTimeStr('QATester_UpdatePanelTags')
        r = queryUpdateTag(tagid, tagGroup, newName)
        self.assertEqual(r["data"]["updateTag"]["group"], tagGroup)
        self.assertEqual(r["data"]["updateTag"]["id"], tagid)
        self.assertEqual(r["data"]["updateTag"]["value"], newName)

    # 测试更新不存在的tagid
    def test_update_error_panel_tags(self):
        tagGroup = "QATester-UpdatePanelTags"
        tagid = getTimeStr('update_error_tag')
        newName = getTimeStr('QATester_UpdatePanelTags')
        r = queryUpdateTag(tagid, tagGroup, newName)
        self.assertIsNotNone(r["errors"])
