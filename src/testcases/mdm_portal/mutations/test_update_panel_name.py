# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json


class UpdatePanelName(unittest.TestCase):

    def test_update_panel_name(self):
        PanelList = getRandomPanelSNAndName()
        SN = PanelList[0]['SN']
        name = getTimeStr('UpdatePanelNameTest')
        r = queryUpdatePanelName(SN, name)
        self.assertEqual(r['data']['updatePanelName']['name'], name)
