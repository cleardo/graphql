# coding=utf-8
# from nd.rest import unittest
from nd.rest.co_test.nd_case import NdCase
from prome_lib.graphql_query import GraphqlQuery
from config import prome_config as con
import unittest


class ModellList(unittest.TestCase):

    def setUp(self):
        self.m = GraphqlQuery()

    def test_modell_list(self):
        if con.AutoTestMode and con.AutoTestMode is False:
            if con.ModellListTimes and len(con.ModellListTimes) != 0:
                times = con.ModellListTimes
            else:
                times = 1
        else:
            times = 1

        def model_list(i):
            print "#################### Testing %d  Ota ####################" % (i + 1)
            r, b = self.m.modelList()
            self.assertEqual(r.status_code, 200)

        for i in range(times):
            model_list(i)