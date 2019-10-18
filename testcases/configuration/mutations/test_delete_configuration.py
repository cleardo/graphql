# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
from config import prome_config as con


class DeleteConfiguration(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_delete_configuration(self):

        # times = 2
        name = "QATester"
        ConfigurationIdList = self.DO.getConfigurationIdListByName(name)
        lenList = len(ConfigurationIdList)

        def update_configuration(i, configurationId):
            print "############# Testing %d  Delete Configuration #############" % (i + 1)
            print "Delete configuration ConfigurationId is :\n", configurationId
            r, b = self.GQ.deleteConfiguration(configurationId)

            # --------------------断言 assert--------------------
            # 断言API正在运行  assertEqual API server is running
            self.assertEqual(r.status_code, 200)

        for i in range(lenList/2):
            configurationId = ConfigurationIdList[i]
            update_configuration(i, configurationId)


if __name__ == '__main__':
    unittest.main()
