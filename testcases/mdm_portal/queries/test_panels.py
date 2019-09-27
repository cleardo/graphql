# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
import random
from config import prome_config as con


class Panels(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_Panels(self):

        if con.AutoTestMode and con.AutoTestMode is False:

            if con.PanelsTimes and len(con.PanelsTimes):
                times = con.PanelsTimes
            if con.Panels_pagesize and len(con.Panels_pagesize):
                    Panels_pagesize = con.Panels_pagesize
            else:
                Panels_pagesize = 1

            if con.Panels_offset and len(con.Panels_offset):
                    Panels_offset = con.Panels_offset
            else:
                Panels_offset = 1
        else:
            Panels_pagesize = 1
            Panels_offset = 0
            times = 1

        def panels(i, Panels_pagesize, Panels_offset):
            print "#################### Testing %d  Panels ####################" % (i + 1)
            r, b = self.GQ.panels(Panels_pagesize, Panels_offset)

            # --------------------断言 assert--------------------
            # 断言API正在运行  assertEqual API server is running
            self.assertEqual(r.status_code, 200)
            self.assertIsNotNone(b["data"])

        for i in range(times):
            panels(i, Panels_pagesize, Panels_offset)


if __name__ == '__main__':
    unittest.main()
