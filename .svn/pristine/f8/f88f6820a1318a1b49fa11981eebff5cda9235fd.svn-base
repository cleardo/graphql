# coding=utf-8
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
from config import prome_config as con
import unittest
import random


class ActivityLogTest(unittest.TestCase):
    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_activitylogs(self):

        if con.AutoTestMode and con.AutoTestMode is False:

            if con.ActivityLogTestTimes and len(con.ActivityLogTestTimes) != 0:
                times = con.ActivityLogTestTimes
            else:
                times = 1

            if con.ActivityLogTestSN and len(con.ActivityLogTestSN) != 0:
                SN = con.ActivityLogTestSN
            else:
                PanelList = self.DO.getRandomPanelSnAndNameList(times)
                SN = PanelList[i]['serialNumber']
        else:
            times = 1
            PanelList = self.DO.getRandomPanelSnAndNameList(times)

        def activitylogs(i, SN):
            print "#################### Testing %d  ActivityLog ####################" % (i + 1)
            print '\nTesting Get Log Panel SN  is :', SN
            r, b = self.GQ.activityLogs(SN, 1, 0)
            serialNumber = b['data']['ActivityLogs']['logs'][0]['serialNumber']
            name = b['data']['ActivityLogs']['logs'][0]['panelName']
            status = b['data']['ActivityLogs']['logs'][0]['status']
            print '\nTesting Get Log Panel Name  is :', name
            self.assertEqual(r.status_code, 200)
            self.assertEqual(status, "200")
            self.assertEqual(serialNumber, SN)

        for i in range(times):
            if con.AutoTestMode and con.AutoTestMode is False:
                activitylogs(i, SN)
            else:
                SN = PanelList[i]['serialNumber']
                activitylogs(i, SN)
