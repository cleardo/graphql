# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
from config import prome_config as con


class GetAppliedPanel(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_get_applied_panel(self):

        times = 1
        Description = "QATester_create_configuration"
        ConfigurationIdList = self.DO.getConfigurationIdListByDescription(Description)

        def get_applied_panel(i, configurationId):
            print "#################### Testing %d  GetApplied Panel ####################" % (i + 1)
            print "Get Applied Panel ID is ", configurationId
            r, b = self.GQ.getAppliedPanel(configurationId)

            # --------------------断言 assert--------------------
            # 断言API正在运行  assertEqual API server is running
            self.assertEqual(r.status_code, 200)

        for i in range(times):
            configurationId = ConfigurationIdList[i]
            get_applied_panel(i, configurationId)


if __name__ == '__main__':
    unittest.main()
