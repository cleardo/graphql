# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json


class EnrollAndUnenroll(unittest.TestCase):

    def test_enroll_panel(self):
        PanelList = getRandomPanelSNAndName()
        SN = PanelList[0]['SN']

        def unenroll():
            r = queryUnenroll(SN)
            self.assertIsNone(r['data']['unenroll'][0]['error'])
            self.assertEqual(r['data']['unenroll'][0]['serialNumber'], SN)
            self.assertIs(r['data']['unenroll'][0]['unenrolled'], True)

        unenroll()

        def enroll():
            panelName = "QATester-enroll"
            r = queryEnroll(SN, panelName=panelName)
            self.assertIs(r['data']['enroll'][0]['enrolled'], True)
            self.assertIsNone(r['data']['enroll'][0]['error'])
            self.assertEqual(r['data']['enroll'][0]['panelName'], panelName)
            self.assertEqual(r['data']['enroll'][0]['serialNumber'], SN)

        enroll()
