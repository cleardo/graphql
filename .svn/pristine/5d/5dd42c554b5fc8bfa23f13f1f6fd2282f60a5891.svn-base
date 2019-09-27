# coding =utf-8

import unittest
from prome_lib.enroll_graphql_query import BatchEnroll


class BatchUnEnroll(unittest.TestCase):

    def setUp(self):
        self.m = BatchEnroll()

    def test_un_enroll_v1_ok_one(self):                   # un enroll one device successfully
        # prepare data
        # send request
        response, body = self.m.unenroll("MockSeria110")
        # print(body)
        un_enroll_validation_list = body['data']['unenroll']
        un_enrolled = un_enroll_validation_list[0]['unenrolled']
        error = un_enroll_validation_list[0]['error']

        # result verification
        self.assertEqual(response.status_code, 200)  # request succeed
        self.assertEqual(un_enrolled, True)  # un enroll succeed
        # self.assertIsNotNone(error)       # error message is not empty
        print(error)                         # print error message

    def test_un_enroll_v2_ok_batch(self):                    # un enroll batch devices successfully
        # prepare data
        filename = 'bulk_unenroll_correct_data.CSV'
        # send request
        response, body = self.m.bulk_unenroll(str(filename))

        # print(body)
        self.assertEqual(response.status_code, 200)
        un_enroll_validation_list = body['data']['unenroll']
        for i in un_enroll_validation_list:
            un_enrolled = i['unenrolled']
            error = i['error']
            self.assertEqual(un_enrolled, True)
            self.assertIsNone(error)
            print(error)
        # print(response)

        # result verification
          # request succeed
          # un enroll succeed
          # error message is not empty
          # print error message

    def test_un_enroll_v3_fail_unenrolled(self):            # un enroll an already un_enrolled device'll fail
        # prepare data
        # send request
        response, body = self.m.unenroll("MockSeria110")
        # print(body)
        un_enroll_validation_list = body['data']['unenroll']
        un_enrolled = un_enroll_validation_list[0]['unenrolled']
        error = un_enroll_validation_list[0]['error']

        # result verification
        self.assertEqual(response.status_code, 200)  # request succeed
        self.assertEqual(un_enrolled, False)  # un enroll succeed
        self.assertIsNotNone(error)       # error message is not empty
        print(error)                         # print error message

    def test_un_enroll_v4_fail_sn(self):                    # un enroll a device which sn doesn't exit in device server
        # prepare data
        # send request
        response, body = self.m.unenroll("MockSeria110")
        # print(body)
        un_enroll_validation_list = body['data']['unenroll']
        un_enrolled = un_enroll_validation_list[0]['unenrolled']
        error = un_enroll_validation_list[0]['error']

        # result verification
        self.assertEqual(response.status_code, 200)  # request succeed
        self.assertEqual(un_enrolled, False)  # un enroll succeed
        self.assertIsNotNone(error)  # error message is not empty
        print(error)                    # print error message

    def test_un_enroll_v5_fail_partly(self):               # un enroll 10 devices,partly fail
        # prepare data, 3 devices are already un_enrolled, 3 devices' sn doesn't exit, 4 devices are good to go
        filename = 'unenroll_partly_fail_data.CSV'
        # send request
        response, body = self.m.bulk_unenroll(str(filename))
        # print(body)
        # un_enroll_validation_list = body['data']['unenroll']

        # result verification
        self.assertEqual(response.status_code, 200)  # request succeed
        # self.assertEqual(un_enrolled, False)  # un enroll succeed
        # self.assertIsNotNone(error)  # error message is not empty
        print(body)                  # print error message

    def test_un_enroll_v6_fail_all(self):            # un enroll 10 devices all fail
        # prepare data, 5 devices are already un_enrolled, 5 devices' sn doesn't exit
        filename = 'unenroll_all_fail_data.CSV'
        # send request
        response, body = self.m.bulk_unenroll(str(filename))
        # print(body)
        un_enroll_validation_list = body['data']['unenroll']
        self.assertEqual(response.status_code, 200)
        print(body)

        # 判断结果
        for i in un_enroll_validation_list:
            unenrolled = i['unenrolled']
            error = i['error']
            self.assertEqual(unenrolled, False)
            self.assertIsNotNone(error)
            print(error)