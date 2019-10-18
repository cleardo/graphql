# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
from config import prome_config as con


class GetDeployConfig(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_get_deploy_config(self):

        times = 1
        PanelList = self.DO.getRandomPanelSnAndNameList(1)

        def get_deploy_config(i, serialNumber):
            print "#################### Testing %d  GetDeploy Config ####################" % (i + 1)
            print "Get Deploy Config SN is ", serialNumber
            r, b = self.GQ.getDeployConfig(serialNumber)

            # --------------------断言 assert--------------------
            # 断言API正在运行  assertEqual API server is running
            self.assertEqual(r.status_code, 200)

        for i in range(times):
            serialNumber = PanelList[i]['serialNumber']
            get_deploy_config(i, serialNumber)


if __name__ == '__main__':
    unittest.main()
