# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json


class Ota(unittest.TestCase):

    def test_ota(self):
        r = queryOta()
        self.assertIsNotNone(r["data"])
