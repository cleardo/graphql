# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
from config import prome_config as con


class Reapply(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_reapply(self):

        Description = "QATester_update_configuration"
        ConfigurationIdList = self.DO.getConfigurationIdListByDescription(Description)

        print "############# Testing %d  Reapply Configuration #############"
        print "Update configuration ConfigurationId is :\n", ConfigurationIdList[0]
        r, b = self.GQ.reapply(ConfigurationIdList[0], "true")

        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
