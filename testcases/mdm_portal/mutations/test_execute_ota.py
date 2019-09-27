# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
from config import prome_config as con


class TestExecuteOta(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_execute_ota(self):
        times = 1
        PanelList = self.DO.getRandomPanelSnAndNameList(times)

        def execute_ota(i):
            serialNumber = PanelList[i]['serialNumber']
            name = PanelList[i]['name']
            print "####################Testing %d Execute Ota####################" % (i + 1)
            print '\nTesting Execute Ota SN  is :', serialNumber
            print '\nTesting Execute Ota Name  is :', name
            r, b = self.GQ.executeOta(serialNumber)
            self.assertEqual(r.status_code, 200)
            self.assertEquals(b['data']['executeOta'], 'success')

        for i in range(times):
            execute_ota(i)
