# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
import random
from config import prome_config as con


class ExecuteAppInstall(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_executeAppInstall(self):

        times = 1
        PanelList = self.DO.getRandomPanelSnAndNameList(times)
        apk_url = "https://alissl.ucdl.pp.uc.cn/fs08/2017/05/24/11/115_9fb5a9e9649d9330c952e2a5c3a10f49.apk"

        def executeAppInstall(i):
            """
            :return:
            """
            serialNumber = PanelList[i-1]['serialNumber']
            print "########## Testing %d executeAppInstall ##########" % (i + 1)
            response, body = self.GQ.executeAppInstall(serialNumber, apk_url)
            print(body)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(body['data']['executeAppInstall']['result'], 'success')

        for i in range(times):
            executeAppInstall(i)
