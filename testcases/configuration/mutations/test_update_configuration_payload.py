# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
from config import prome_config as con


class UpdateConfigurationPayload(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_update_configuration_payload(self):

        times = 1
        frequency = "week"
        dayOfWeek = 1
        time = "17:00"
        description = "QATester_create_configuration"
        IdList = self.DO.getConfigurationIdListByDescription(description)

        def update_configuration_payload(i, configurationId, frequency, dayOfWeek, time):
            print "######### Testing %d  Update Configuration Payload #########" % (i + 1)
            print "Update Payload configurationId is ", configurationId
            r, b = self.GQ.updateConfigurationPayload(configurationId, frequency, dayOfWeek, time)

            # --------------------断言 assert--------------------
            # 断言API正在运行  assertEqual API server is running
            self.assertEqual(r.status_code, 200)
            autoOff = b['data']['updateConfigurationPayload']['configPayload']['autoOff']
            self.assertEqual(autoOff['dayOfWeek'], dayOfWeek)
            self.assertEqual(autoOff['frequency'], frequency)
            self.assertEqual(autoOff['time'], time)

        for i in range(times):
            configurationId = IdList[i]
            update_configuration_payload(i, configurationId, frequency, dayOfWeek, time)


if __name__ == '__main__':
    unittest.main()
