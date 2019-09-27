# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
import random
from config import prome_config as con

class MainboardFirmwareList(unittest.TestCase):
    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_main_board_firmware_list(self):

        if con.AutoTestMode and con.AutoTestMode is False:

            if con.MainboardFirmwareListTimes and len(con.MainboardFirmwareListTimes) != 0:
                times = con.MainboardFirmwareListTimes
            else:
                times = 1
        else:
            times = 1

        def main_board_firmware_list(i):
            print "############ Testing %d  MainboardFirmwareList ############" % (i + 1)
            r, b = self.GQ.mainboardFirmwareList()
            self.assertEqual(r.status_code, 200)
            self.assertIsNotNone(b['data'])

        for i in range(times):
            main_board_firmware_list(i)
