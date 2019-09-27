# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
from config import prome_config as con


class ConfigurationList(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_configurationList(self):

        times = 1
        pageNumber = 1
        pageSize = 1

        def configurationList(i, pageNumber, pageSize):
            print "#################### Testing %d  configurationList ####################" % (i + 1)
            r, b = self.GQ.configurationList(pageNumber, pageSize)

            # --------------------断言 assert--------------------
            # 断言API正在运行  assertEqual API server is running
            self.assertEqual(r.status_code, 200)

        for i in range(times):
            configurationList(i, pageNumber, pageSize)


if __name__ == '__main__':
    unittest.main()
