# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
import random
from config import prome_config as con

class EnrollValidation(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    # 验证 SN 已注册的面板
    def test_enrolled_panel(self):
        if con.AutoTestMode and con.AutoTestMode is False:

            if con.test_enrolled_panel_times and len(con.test_enrolled_panel_times) != 0:
                times = con.test_enrolled_panel_times
            else:
                times = 1

            if con.test_enrolled_panel_SN and len(con.test_enrolled_panel_SN) and \
                    con.test_enrolled_panel_Name and len(con.test_enrolled_panel_Name) != 0:
                SN = con.test_enrolled_panel_SN
                name = con.test_enrolled_panel_Name
            else:
                PanelList = self.DO.getRandomPanelSnAndNameList(1)
                SN = PanelList[0]['serialNumber']
                name = PanelList[0]['name']
        else:
            times = 1

        def enrolled_panel(i, SN, name):
            # 发送请求
            print "#################### Testing %d  Enrolled Panel ####################" % (i + 1)
            print '\nTesting Enrolled Panel SN  is :', SN
            print '\nTesting Enrolled Panel Name  is :', name
            response, body = self.GQ.enroll_validation(SN, name)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(body['data']['EnrollValidation'][0]['isValid'], False)
            self.assertEqual(body['data']['EnrollValidation'][0]['error'], "Panel already enrolled")

        for i in range(times):
            if con.AutoTestMode and con.AutoTestMode is False:
                enrolled_panel(i, SN, name)
            else:
                PanelList = self.DO.getRandomPanelSnAndNameList(1)
                SN = PanelList[0]['serialNumber']
                name = PanelList[0]['name']
                enrolled_panel(i, SN, name)

    # SN和panel name都不存在于device server，查询返回false
    def test_error_SN_and_name(self):
        # 准备数据
        if con.AutoTestMode and con.AutoTestMode is False:

            if con.test_error_SN_and_name_times and len(con.test_error_SN_and_name_times) != 0:
                times = con.test_error_SN_and_name_times
            else:
                times = 1

            if con.test_error_SN_and_name_SN and len(con.test_error_SN_and_name_SN) and \
                    con.test_error_SN_and_name_Name and len(con.test_error_SN_and_name_Name) != 0:
                SN = con.test_error_SN_and_name_SN
                name = con.test_error_SN_and_name_Name
            else:
                SN = "3241f3qwfsdaa1eaad"
                name = "vasrdcsaf"
        else:
            times = 1
            SN = "3241f3qwfsdaa1eaad"
            name = "vasrdcsaf"

        # 发送请求
        def error_SN_and_name(SN, name):
            print "## Testing %d  SN and name not existed to device server ##" % (i + 1)
            print '\nTesting not existed Panel SN  is :', SN
            print '\nTesting not existed Panel Name  is :', name
            response, body = self.GQ.enroll_validation(SN, name)
            enroll_validation_list = body['data']['EnrollValidation']
            isValid = enroll_validation_list[0]['isValid']
            error = enroll_validation_list[0]['error']
            # 判断结果
            self.assertEqual(response.status_code, 200)  # 判断请求是否成功
            self.assertEqual(isValid, False)   # 判断SN码是否有效
            self.assertIsNotNone(error)       # 判断error为空

        for i in range(times):
            error_SN_and_name(SN, name)
    # SN不存在于device server，panel name存在，查询返回false

    # 验证错误的 SN 和正确的 name 返回false
    def test_error_SN_and_true_name(self):
        # 准备数据
        if con.AutoTestMode and con.AutoTestMode is False:

            if con.test_error_SN_and_true_name_times and len(con.test_error_SN_and_true_name_times) != 0:
                times = con.test_error_SN_and_true_name_times
            else:
                times = 1

            if con.test_error_SN_and_true_name_SN and len(con.test_error_SN_and_true_name_SN) and \
                    con.test_error_SN_and_true_name_Name and len(con.test_error_SN_and_true_name_Name) != 0:
                SN = con.test_error_SN_and_true_name_SN
                name = con.test_error_SN_and_true_name_Name
            else:
                PanelList = self.DO.getRandomPanelSnAndNameList(1)
                SN = "sadfjilkscnmsal12390jdsoifhj210h1nassd"
                name = PanelList[0]['name']
        else:
            times = 1
            PanelList = self.DO.getRandomPanelSnAndNameList(1)
            SN = "sadfjilkscnmsal12390jdsoifhj210h1nassd"
            name = PanelList[0]['name']

        # 发送请求
        def error_SN_and_true_name(SN, name):
            print "####### Testing %d  error SN and true name #######" % (i + 1)
            print '\nTesting error Panel SN  is :', SN
            print '\nTesting true Panel Name  is :', name
            response, body = self.GQ.enroll_validation(SN, name)
            enroll_validation_list = body['data']['EnrollValidation']
            isValid = enroll_validation_list[0]['isValid']
            error = enroll_validation_list[0]['error']
            self.assertEqual(response.status_code, 200)  # 判断请求是否成功
            self.assertEqual(isValid, False)   # 判断SN码是否有效
            self.assertIsNotNone(error)       # 判断error是否有值

        for i in range(times):
            error_SN_and_true_name(SN, name)

    # 验证正确的 SN 和错误的 name 返回false
    def test_true_SN_and_error_name(self):
        # 准备数据
        if con.AutoTestMode and con.AutoTestMode is False:

            if con.test_true_SN_and_error_name_times and len(con.test_true_SN_and_error_name_times) != 0:
                times = con.test_true_SN_and_error_name_times
            else:
                times = 1

            if con.test_true_SN_and_error_name_SN and len(con.test_true_SN_and_error_name_SN) and \
                    con.test_true_SN_and_error_name_Name and len(con.test_true_SN_and_error_name_Name) != 0:
                SN = con.test_true_SN_and_error_name_SN
                name = con.test_true_SN_and_error_name_Name
            else:
                PanelList = self.DO.getRandomPanelSnAndNameList(1)
                SN = PanelList[0]['serialNumber']
                name = "sadfjilkqwe11111111111j210h1nassd"
        else:
            times = 1
            PanelList = self.DO.getRandomPanelSnAndNameList(1)
            SN = PanelList[0]['serialNumber']
            name = "sadfjilkqwe11111111111j210h1nassd"

        # 发送请求
        def true_SN_and_error_name(SN, name):
            print "####### Testing %d  true SN and error name #######" % (i + 1)
            print '\nTesting true Panel SN  is :', SN
            print '\nTesting error Panel Name  is :', name
            response, body = self.GQ.enroll_validation(SN, name)
            enroll_validation_list = body['data']['EnrollValidation']
            isValid = enroll_validation_list[0]['isValid']
            error = enroll_validation_list[0]['error']
            self.assertEqual(response.status_code, 200)  # 判断请求是否成功
            self.assertEqual(isValid, False)   # 判断SN码是否有效
            self.assertIsNotNone(error)       # 判断error是否有值

        for i in range(times):
            true_SN_and_error_name(SN, name)

    # 验证 未注册SN 可注册
    def test_existed_device_server_SN(self):
        # 指定参数模式，设置参数
        if con.AutoTestMode and con.AutoTestMode is False:

            if con.test_existed_device_server_SN_times and \
                    len(con.test_existed_device_server_SN_times) != 0:
                times = con.test_existed_device_server_SN_times
            else:
                times = 1

            if con.test_existed_device_server_SN and len(con.test_existed_device_server_SN) != 0:
                SNList = con.test_existed_device_server_SNList
            else:
                HavaunenrollPanel is True
                PanelList = self.DO.getRandomPanelSnAndNameList(1)
                SN = PanelList[i]['serialNumber']
                self.GQ.unenroll(SN, showprint=False)

            # 验证 未注册的SN可注册
            def enroll_validation_existed_SN(i, SN):
                print "\n####### Testing %d not enroll SN #######" % (i + 1)
                print " \nNot enroll Panel SN is :", SN
                panelName = self.DO.getTimeStr("name must be enter :")
                response, body = self.GQ.enroll_validation(SN, panelName)
                enroll_validation_list = body['data']['EnrollValidation']
                isValid = enroll_validation_list[0]['isValid']
                error = enroll_validation_list[0]['error']
                self.assertEqual(response.status_code, 200)  # 判断请求是否成功
                self.assertEqual(isValid, True)  # 判断SN码是否有效
                self.assertIsNone(error)  # 判断error是否有值
                if HavaunenrollPanel is True:
                    panelName = self.DO.getTimeStr("enroll success at :")
                    self.GQ.enroll(SN, panelName, showprint=False)
            for i in range(times):
                if con.AutoTestMode and con.AutoTestMode is False:
                    for j in range(len(SNList)):
                        SN = SNList[j]
                        enroll_validation_existed_SN(j, SN)
                else:
                    enroll_validation_existed_SN(i, SN)

        # 自动模式， 获取已注册面板，解除注册--> 验证未注册--> 再注册
        else:
            times = 1
            PanelList = self.DO.getRandomPanelSnAndNameList(times)

            # 先解注册
            def unenroll(i):
                SN = PanelList[i]['serialNumber']
                r, b = self.GQ.unenroll(SN, showprint=False)
                self.assertEqual(r.status_code, 200)
                self.assertIsNone(b['data']['unenroll'][0]['error'])
                self.assertEqual(b['data']['unenroll'][0]['serialNumber'], SN)
                self.assertIs(b['data']['unenroll'][0]['unenrolled'], True)

            # 验证 解除注册的SN可注册
            def enroll_validation_existed_SN(i):
                serialNumber = PanelList[i]['serialNumber']
                panelName = self.DO.getTimeStr("")
                # 发送请求
                print "\n####### Testing %d enroll_validation_existed_SN #######" % (i + 1)
                print " \nNot enroll Panel SN is :", serialNumber
                response, body = self.GQ.enroll_validation(serialNumber, panelName)
                enroll_validation_list = body['data']['EnrollValidation']
                isValid = enroll_validation_list[0]['isValid']
                error = enroll_validation_list[0]['error']
                self.assertEqual(response.status_code, 200)  # 判断请求是否成功
                self.assertEqual(isValid, True)  # 判断SN码是否有效
                self.assertIsNone(error)  # 判断error是否有值

            # 验证后注册
            def enroll(i):
                SN = PanelList[i]['serialNumber']
                panelName = self.DO.getTimeStr("enroll success at :")
                r, b = self.GQ.enroll(SN, panelName, showprint=False)
                self.assertEqual(r.status_code, 200)
                self.assertIs(b['data']['enroll'][0]['enrolled'], True)
                self.assertIsNone(b['data']['enroll'][0]['error'])
                self.assertEqual(b['data']['enroll'][0]['panelName'], panelName)
                self.assertEqual(b['data']['enroll'][0]['serialNumber'], SN)

            for i in range(times):
                unenroll(i)
                enroll_validation_existed_SN(i)
                enroll(i)
