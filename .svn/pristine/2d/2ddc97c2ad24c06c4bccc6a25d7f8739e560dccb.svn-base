# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
import time
from config import prome_config as con


class UpdatePanelName(unittest.TestCase):
    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_update_panel_name(self):

        if con.AutoTestMode and con.AutoTestMode is False:

            if con.test_update_panel_name_times and len(con.test_update_panel_name_times) != 0:
                times = con.test_update_panel_name_times
            else:
                times = 1

            if con.test_update_panel_name_SN and len(con.test_update_panel_name_SN) != 0 and \
                    con.test_update_panel_name_Name and len(con.test_update_panel_name_Name):
                SN = con.test_update_panel_name_SN
                name = con.test_update_panel_name_Name
            else:
                PanelList = self.DO.getRandomPanelSnAndNameList(times)
                SN = PanelList[0]['serialNumber']
        else:
            times = 1
            PanelList = self.DO.getRandomPanelSnAndNameList(times)
            name = self.DO.getTimeStr('QATest_updatePanelName')

        def update_panel_name(i, SN, name):
            print "########## Testing %d  Update Panel Name ##########" % (i + 1)
            print '\nupdata serialNumber is :', SN
            print '\nupdata name is :', name
            response, body = self.GQ.updatePanelName(SN, name)

            # --------------------断言 assert--------------------
            # 断言API正在运行  assertEqual API server is running
            self.assertEqual(response.status_code, 200)
            # 断言更新 name 成功
            self.assertEquals(body['data']['updatePanelName']['name'], name)

        for i in range(times):
            if con.AutoTestMode and con.AutoTestMode is False:
                update_panel_name(i, SN, name)
            else:
                SN = PanelList[0]['serialNumber']
                update_panel_name(i, SN, name)

