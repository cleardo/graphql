# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
from config import prome_config as con


class ConfigurationDetail(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_configuration_detail(self):

        times = 3

        def configurationDetail(i, configurationId):
            print "#################### Testing %d  ConfigurationDetail ####################" % (i + 1)
            print "Test configurationId is ", configurationId
            r, b = self.GQ.configurationDetail(configurationId)

            # --------------------断言 assert--------------------
            # 断言API正在运行  assertEqual API server is running
            self.assertEqual(r.status_code, 200)

        for i in range(times):
            configurationIdList = self.DO.getRandomConfigurationIdList(times)
            configurationId = configurationIdList[i]
            configurationDetail(i, configurationId)


if __name__ == '__main__':
    unittest.main()
