# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
import random
from config import prome_config as con


class EnrollAndUnenroll(unittest.TestCase):
    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_enroll_panel(self):
        times = 1
        PanelList = self.DO.getRandomPanelSnAndNameList(times)
        panelName = self.DO.getTimeStr("enroll success at :")

        def unenroll(i):
            SN = PanelList[i]['serialNumber']
            print "\n####################Testing %d unenroll####################" % (i + 1)
            print "\nunenroll Panel SN is :", SN
            r, b = self.GQ.unenroll(SN)
            self.assertEqual(r.status_code, 200)
            self.assertIsNone(b['data']['unenroll'][0]['error'])
            self.assertEqual(b['data']['unenroll'][0]['serialNumber'], SN)
            self.assertIs(b['data']['unenroll'][0]['unenrolled'], True)

        def enroll(i):
            SN = PanelList[i]['serialNumber']
            print "\n####################Testing %d enroll####################" % (i + 1)
            print " \nenroll Panel SN is :", SN
            print " \nenroll Panel Name is :", panelName
            r, b = self.GQ.enroll(SN, panelName)
            self.assertEqual(r.status_code, 200)
            self.assertIs(b['data']['enroll'][0]['enrolled'], True)
            self.assertIsNone(b['data']['enroll'][0]['error'])
            self.assertEqual(b['data']['enroll'][0]['panelName'], panelName)
            self.assertEqual(b['data']['enroll'][0]['serialNumber'], SN)

        for i in range(times):
            unenroll(i)
            enroll(i)
