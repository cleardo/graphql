# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json


class ModellList(unittest.TestCase):

    def test_modell_list(self):
        r = queryModelList()
        self.assertIsNotNone(r["data"]["ModelList"])
