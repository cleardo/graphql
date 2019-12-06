# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json


class Panels(unittest.TestCase):

    def test_Panels(self):
        r = queryPanels(pageSize=5, offset=0)
        self.assertEqual(len(r["data"]["Panels"]["panels"]), 5)


if __name__ == '__main__':
    unittest.main()
