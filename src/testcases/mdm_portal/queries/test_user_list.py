# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json


class UserList(unittest.TestCase):

    def test_user_list(self):
        r = queryUserList()
        self.assertIsNotNone(r["data"]["UserList"])

