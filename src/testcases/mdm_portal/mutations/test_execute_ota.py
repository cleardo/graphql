# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json


class TestExecuteOta(unittest.TestCase):

    def test_execute_ota(self):
        queryOta()
