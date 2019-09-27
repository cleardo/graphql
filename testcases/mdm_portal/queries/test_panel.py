# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
from config import prome_config as con


class Panel(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_Panel(self):

        # 设置数据
        if con.AutoTestMode and con.AutoTestMode is False:
            # 设置测试次数
            if con.PanelTimes and len(con.PanelTimes):
                    times = con.PanelTimes
            else:
                times = 1

            # 设置指定SN
            if con.PanelSN and len(con.PanelSN):
                    PanelSN = con.PanelSN
            else:
                PanelList = self.DO.getRandomPanelSnAndNameList(times)
                PanelSN = PanelList[0]['serialNumber']
        else:
            times = 1
            PanelList = self.DO.getRandomPanelSnAndNameList(times)
            PanelSN = PanelList[0]['serialNumber']

        # 查询
        def panel(i, SN):
            print "#################### Testing %d Panel ####################" % (i + 1)
            print '\nTesting Get Panelinfo SN  is :', SN
            response, body = self.GQ.panel(SN)
            name = body['data']['Panel']['summary']['name']
            print '\nTesting Get Panelinfo Name  is :', name
            # --------------------断言 assert--------------------
            # 断言API正在运行  assertEqual API server is running
            self.assertEqual(response.status_code, 200)

        for i in range(times):
            panel(i, PanelSN)


if __name__ == '__main__':
    unittest.main()
