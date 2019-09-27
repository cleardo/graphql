# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
from config import prome_config as con


class UpdateConfiguration(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_update_configuration(self):

        times = 3
        getName = "QATester_create_configuration"
        ConfigurationIdList = self.DO.getConfigurationIdListByDescription(getName)
        name = "QATester_update_configuration"

        def update_configuration(i, configurationId, name, description):
            print "############# Testing %d  Update Configuration #############" % (i + 1)
            print "Update configuration ConfigurationId is :\n", configurationId
            print "\nUpdate configuration name is :\n", name
            r, b = self.GQ.updateConfiguration(configurationId, name, description)

            # --------------------断言 assert--------------------
            # 断言API正在运行  assertEqual API server is running
            self.assertEqual(r.status_code, 200)

        for i in range(times):
            description = self.DO.getTimeStr("QATester_update_configuration")
            configurationId = ConfigurationIdList[i]
            update_configuration(i, configurationId, name, description)


if __name__ == '__main__':
    unittest.main()
