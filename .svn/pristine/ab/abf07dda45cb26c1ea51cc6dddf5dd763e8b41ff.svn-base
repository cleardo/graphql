# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
from config import prome_config as con


class GetAppliedPanel(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_get_applied_panel(self):

        times = 1
        Description = "QATester_create_configuration"
        ConfigurationIdList = self.DO.getConfigurationIdListByDescription(Description)

        def get_applied_panel(i, configurationId):
            print "#################### Testing %d  GetApplied Panel ####################" % (i + 1)
            print "Get Applied Panel ID is ", configurationId
            r, b = self.GQ.getAppliedPanel(configurationId)

            # --------------------断言 assert--------------------
            # 断言API正在运行  assertEqual API server is running
            self.assertEqual(r.status_code, 200)

        for i in range(times):
            configurationId = ConfigurationIdList[i]
            get_applied_panel(i, configurationId)

    def test_not_applied_of_Panel(self):

        # premise
        name = self.DO.getTimeStr("QATest")
        description = "QATester_create_configuration"
        r, b = self.GQ.createConfiguration(name, description, showprint=False)
        configurationId = b['data']['createConfiguration']['configurationId']

        # test strat
        print "#################### Testing  GetApplied Panel ####################"
        print "Get Applied Panel ID is ", configurationId
        r, b = self.GQ.getAppliedPanel(configurationId)

        #  assert

        self.assertEqual(r.status_code, 200)
        self.assertEqual(b['data']['getAppliedPanel']['panels'], [])

    def test_applied_of_Panel(self):

        # premise
        name = self.DO.getTimeStr("QATest")
        description = "QATester_create_configuration"
        r, b = self.GQ.createConfiguration(name, description, showprint=False)
        configurationId = b['data']['createConfiguration']['configurationId']
        PanelList = self.DO.getRandomPanelSnAndNameList()
        serialNumber = PanelList[0]['serialNumber']
        panelName = PanelList[0]['name']
        self.GQ.deployConfiguration(serialNumber, configurationId)

        # test strat
        print "#################### Testing  GetApplied Panel ####################"
        print "Get Applied Panel ID is ", configurationId
        r, b = self.GQ.getAppliedPanel(configurationId)

        #  assert
        self.assertEqual(r.status_code, 200)
        self.assertEqual(b['data']['getAppliedPanel']['panels'][0]['panelName'], panelName)
        self.assertEqual(b['data']['getAppliedPanel']['panels'][0]['serialNumber'], serialNumber)


if __name__ == '__main__':
    unittest.main()
