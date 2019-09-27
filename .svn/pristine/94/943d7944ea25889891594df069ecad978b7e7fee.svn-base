# coding =utf-8

import unittest
from prome_lib.enroll_graphql_query import BatchEnroll


class UnEnrollData(unittest.TestCase):

    def setUp(self):
        self.m = BatchEnroll()
        """
        Clear data to make sure all the serial number and panel name is usable, not enrolled
        """

    def test_un_enroll_data(self):  # un enroll batch devices successfully
        # prepare data
        filename = 'clear_data.CSV'
        # send request
        response, body = self.m.bulk_unenroll(str(filename))
        self.assertEqual(response.status_code, 200)
        print(body)
