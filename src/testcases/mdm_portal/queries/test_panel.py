# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json


class Panel(unittest.TestCase):

    def test_Panel(self):
        PanelList = getRandomPanelSNAndName()
        SN = PanelList[0]['SN']
        name = PanelList[0]['name']
        r = queryPanel(SN)
        self.assertEqual(r["data"]["Panel"]["summary"]["name"], name)
        self.assertEqual(r["data"]["Panel"]["summary"]["serialNumber"], SN)


if __name__ == '__main__':
    unittest.main()
