# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
import random
from config import prome_config as con


class UserList(unittest.TestCase):
    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_user_list(self):

        if con.AutoTestMode and con.AutoTestMode is False:

            if con.UserListTimes and len(con.UserListTimes) != 0:
                times = con.UserListTimes
            else:
                times = 1
        else:
            times = 1

        def user_list(i):
            print "#################### Testing %d UserList ####################" % (i + 1)
            r, b = self.GQ.userList()
            self.assertEqual(r.status_code, 200)

        for i in range(times):
            user_list(i)
