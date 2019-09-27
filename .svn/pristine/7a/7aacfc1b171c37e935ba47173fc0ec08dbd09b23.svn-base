# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
import random
from config import prome_config as con


class Ota(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_ota(self):
        if con.AutoTestMode and con.AutoTestMode is False:
            if con.TagsTimes and len(con.TagsTimes):
                times = con.TagsTimes
            else:
                times = 1
        else:
            times = 1

        def ota(i):
            """
            查询升级信息
            :return:
            """
            print "#################### Testing %d Ota ####################" % (i+1)
            response, body = self.GQ.ota()
            self.assertEqual(response.status_code, 200)

        for i in range(times):
            ota(i)
