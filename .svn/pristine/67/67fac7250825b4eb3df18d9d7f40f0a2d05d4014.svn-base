# coding=utf-8

import unittest
from prome_lib.enroll_graphql_query import BatchEnroll


class DeviceBatchEnroll(unittest.TestCase):

    def setUp(self):
        self.m = BatchEnroll()

    # 注册一台    Enroll single device
    def test_enroll_v1_ok_one(self):              # 成功enroll一台设备
        # 准备数据
        # 发送请求
        response, body = self.m.enroll("MockSeria110", "MockSeria110")
        enroll_validation_list = body['data']['enroll']
        # enrolled = enroll_validation_list[0]['enrolled']
        error = enroll_validation_list[0]['error']

        # 判断结果
        self.assertEqual(response.status_code, 200)  # 判断请求成功
        # self.assertEqual(enrolled, True)   # 判断enroll成功
        # self.assertIsNotNone(error)       # 判断error有值
        print '----- Error Info ----\n', error, '\n----- Error End -----' # 打印error内容

    # 通过csv批量注册多台   Enroll multiple device by csv file
    def test_enroll_v2_ok_multiple(self):        # 成功批量enroll设备
        # 准备数据
        filename = 'batch_correct_data.CSV'
        # 发送请求
        response, body = self.m.bulk_enroll(str(filename))
        # print(body)
        enroll_validation_list = body['data']['enroll']
        # print(response)

        # 判断结果
        for i in enroll_validation_list:
            enrolled = i['enrolled']
            error = i['error']
            self.assertEqual(enrolled, True)
            self.assertIsNone(error)
            print '----- Error Info ----\n', error, '\n----- Error End -----'  # 打印error内容

    # 传入错误的sn 响应Panel not found.
    def test_enroll_v3_fail_sn(self):           # enroll一台设备失败，SN不存在于device server
        # 准备数据
        # 发送请求
        response, body = self.m.enroll("1234567890", "MockSeria101")
        print(body)
        enroll_validation_list = body['data']['enroll']
        enrolled = enroll_validation_list[0]['enrolled']
        error = enroll_validation_list[0]['error']
        print(response)

        # 判断结果
        self.assertEqual(response.status_code, 200)  # 判断请求成功
        self.assertEqual(enrolled, False)  # 判断是否enroll失败
        self.assertIsNotNone(error)  # 判断error有值
        print '----- Error Info ----\n', error, '\n----- Error End -----' # 打印error内容

    def test_enroll_v4_fail_name(self):            # enroll一台设备失败，panel name不存在于device server
        # 准备数据
        # 发送请求
        response, body = self.m.enroll("MockSeria101", "test0")
        print(body)
        enroll_validation_list = body['data']['enroll']
        enrolled = enroll_validation_list[0]['enrolled']
        error = enroll_validation_list[0]['error']
        print(response)

        # 判断结果
        self.assertEqual(response.status_code, 200)  # 判断请求成功
        self.assertEqual(enrolled, False)  # 判断是否enroll失败
        self.assertIsNotNone(error)  # 判断error有值
        print '----- Error Info ----\n', error, '\n----- Error End -----' # 打印error内容

    def test_enroll_v5_fail_enrolled(self):          # enroll一台已经enroll成功的设备
        # 准备数据
        # 发送请求
        response, body = self.m.enroll("MockSeria110", "MockSeria110")
        print(body)
        enroll_validation_list = body['data']['enroll']
        enrolled = enroll_validation_list[0]['enrolled']
        error = enroll_validation_list[0]['error']
        print(response)

        # 判断结果
        self.assertEqual(response.status_code, 200)  # 判断请求成功
        self.assertEqual(enrolled, False)  # 判断是否enroll失败
        self.assertIsNotNone(error)  # 判断error有值
        print '----- Error Info ----\n', error, '\n----- Error End -----' # 打印error内容

    def test_enroll_v6_fail_duplicate_name(self):                   # enroll一台SN校验通过，但是panel name已存在
        # 准备数据
        # 发送请求
        response, body = self.m.enroll("MockSeria101", "MockSeria110")
        enroll_validation_list = body['data']['enroll']
        enrolled = enroll_validation_list[0]['enrolled']
        error = enroll_validation_list[0]['error']

        # 判断结果
        self.assertEqual(response.status_code, 200)  # 判断请求成功
        self.assertEqual(enrolled, False)  # 判断是否enroll失败
        self.assertIsNotNone(error)  # 判断error有值
        print '----- Error Info ----\n', error, '\n----- Error End -----' # 打印error内容

    def test_enroll_v7_fail_partly(self):          # 批量10台enroll部分失败
        # 准备数据，3台SN不存在，3台panel name不存在，1台SN和panel name都不存在，3台SN和panel name存在
        filename = 'enroll_partly_fail_data.CSV'
        # 发送请求
        response, body = self.m.bulk_enroll(str(filename))
        # enroll_validation_list = body['data']['enroll']
        self.assertEqual(response.status_code, 200)

        # 判断结果
        """for i in enroll_validation_list:
            enrolled = i['enrolled']
            error = i['error']
            self.assertEqual(enrolled, True)
            self.assertIsNone(error)
            print(error)
        """

    def test_enroll_v8_fail_all(self):             # 批量10台enroll都失败
        # 准备数据，3台已enroll，3台SN存在但panel name重复，4台SN和panel name都不存在
        filename = 'enroll_all_fail_data.CSV'
        # 发送请求
        response, body = self.m.bulk_enroll(str(filename))
        # print(body)
        enroll_validation_list = body['data']['enroll']
        self.assertEqual(response.status_code, 200)

        # 判断结果
        print '----- Error Info ----\n'  # 打印error内容
        for i in enroll_validation_list:
            enrolled = i['enrolled']
            error = i['error']
            self.assertEqual(enrolled, False)
            self.assertIsNotNone(error)
            print error, '\n'
        print '----- Error End -----'