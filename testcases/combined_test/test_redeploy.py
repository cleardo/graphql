# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
import json
from config import prome_config as con


class Combined2(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test1(self):

        self.global_var = globals()
        self.configurationId = globals()
        self.PanelList = self.DO.getRandomPanelSnAndNameList(5)

        print "\n---------------Combined2 Testcase 1---------------:"
        print "Combined Step:"
        print "Step1: Create a configuration"
        print "Step2: DeployConfiguration Created configuration"
        print "Step3: Get Configurationdetail"

        # step 1
        def create_configuration():
            print "\n#### Setup 1: Created a configuration ####"
            name = self.DO.getTimeStr("QATester_Combined2_Testcase1_Create")
            query = """
mutation{
  createConfiguration(input:{name:"%s",
    description:"This is Combined2 test reapply",
    unique:false,
    parent:"",
    configurationPayload:{
    schma:"v1",
    merged:true,
    configurations:{
    power:{
    	autoOff:{
                frequency:"week"
                dayOfWeek:1
                time:"17:00"}}}}}){
    configurationId,
    name,
    description,
    createBy,
    orgId,
    createTime,
    updateTime,
    status,
    appliedPanels,
    failedInstalls,
    unique,
    configurationPayload,
  }
}
                                    """
            r = self.GQ.send_query(query % name, api='configuration')
            b = json.loads(r.text)
            self.configurationId = b['data']['createConfiguration']['configurationId']
            self.assertEqual(r.status_code, 200)

        # step 2
        def deploy_configuration(i):
            serialNumber = self.PanelList[i]['serialNumber']
            print "#### Setup 2: Deploy Setup1 Created configuration ####"
            print "#### Deploy configurationId: %s ####" % self.configurationId
            print "#### Deploy serialNumbers: %s ####" % serialNumber

            query = """
mutation{
  deployConfiguration(deployRequest:{
    serialNumbers:"%s",
    configurationId:"%s",
    isDelayed:true
  })
}
            """
            r = self.GQ.send_query(query % (serialNumber, self.configurationId), api='configuration')
            b = json.loads(r.text)
            self.assertEqual(r.status_code, 200)

        # step3
        def configuration_detail(i):
            serialNumber = self.PanelList[i]['serialNumber']
            print "#### Setup 3: Get Setup2 Deployed configuration ####"
            print "#### Deploy configurationId: %s ####" % self.configurationId
            query = """
query configurationDetail{
configurationDetail(configurationId: "%s"){
      appliedPanels
  }
}
                        """
            r = self.GQ.send_query(query % self.configurationId, api='configuration')
            b = json.loads(r.text)
            self.assertEqual(b['data']['configurationDetail']['appliedPanels'], (i+1))
            self.assertEqual(r.status_code, 200)

        # Start
        create_configuration()
        for i in range(5):
            deploy_configuration(i)
            configuration_detail(i)
