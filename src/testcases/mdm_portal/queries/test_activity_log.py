# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json


class ActivityLogTest(unittest.TestCase):

    def test_activitylogs(self):
        PanelList = getRandomPanelSNAndName()
        SN = PanelList[0]['SN']
        name = PanelList[0]['name']
        r = queryActivityLogs(SN)

