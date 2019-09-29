# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
import json
from config import prome_config as con


class Combined1(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()
        self.global_var = globals()

    def test1(self):

        print "\n---------------Combined Testcase 1---------------:"
        print "Combined Step:"
        print "Step1: Create a configuration"
        print "Step2: Update Created configuration"

        # step 1
        def create_configuration():
            print "#### Setup 1: Created a configuration ####"
            name = self.DO.getTimeStr("QATester_Combined_Testcase1_Create")
            query = """
        mutation{
            createConfiguration(input:{name:"%s",
            description:"This is the configuration plan created by automation",
            unique:false}){
                configurationId
                name
                description
                createBy
                orgId
                createTime
                updateTime
                status
                appliedPanels
                failedInstalls
                }
        }
                                    """
            r = self.GQ.send_query(query % name, api='configuration')
            b = json.loads(r.text)
            self.global_var['id1'] = (b['data']['createConfiguration']['configurationId'])
            self.assertEqual(r.status_code, 200)

        # step 2
        def update_configuration():
            print "#### Setup 2: Update Setup1 Created configuration ####"
            name = self.DO.getTimeStr("QATester_Combined_Testcase1_Update")
            description = "This is the configuration plan created by automation updated"
            query = """
mutation{
updateConfiguration(configurationId:"%s",input:{name:"%s",
    description:"%s",
        status:"ready",
        configurationPayload:{
        autoOff:{
        frequency:"week"
        dayOfWeek:7
        time:"20:00"}}}){
            configurationId
            name
            description
            createBy
            orgId
            createTime
            updateTime
            status
            appliedPanels
            failedInstalls
            }
}
            """
            r = self.GQ.send_query(query % (self.global_var['id1'], name, description), api='configuration')
            b = json.loads(r.text)
            self.assertEqual(r.status_code, 200)

        create_configuration()
        update_configuration()

    def test2(self):
        print "\n---------------Combined Testcase 2---------------:"
        print "Combined Step:"
        print "Step1: Create a configuration"
        print "Step2: Update Created configuration"

        # step 1
        def create_configuration():
            print "\n#### Setup 1: Create a configuration ####"
            name = self.DO.getTimeStr("QATester_Combined_Testcase2_Create")
            query = """
mutation{
    createConfiguration(input:{name:"%s",
    description:"This is the configuration plan created by automation",
    unique:false}){
        configurationId
        name
        description
        createBy
        orgId
        createTime
        updateTime
        status
        appliedPanels
        failedInstalls
        }
}
                            """
            r = self.GQ.send_query(query % name, api='configuration')
            b = json.loads(r.text)
            self.global_var['id2'] = (b['data']['createConfiguration']['configurationId'])
            self.assertEqual(r.status_code, 200)

        # step 2
        def update_configuration():
            print "\n#### Setup 2: Update Setup1 Created configuration ####"
            query = """
mutation{
updateConfigurationPayload(configurationId:"%s",input:{
configKey:"power",
configPayload:{
autoOff:{
        frequency:"weekday"
        dayOfWeek:1
        time:"19:00"  
        }}}){
            configKey
            configPayload
            }
}
            """
            r = self.GQ.send_query(query % self.global_var['id2'], api='configuration')
            b = json.loads(r.text)
            configKey = b['data']['updateConfigurationPayload']['configKey']
            autoOff = b['data']['updateConfigurationPayload']['configPayload']['autoOff']
            self.assertEqual(r.status_code, 200)
            self.assertEqual(configKey, 'power')
            self.assertEqual(autoOff['dayOfWeek'], 1)
            self.assertEqual(autoOff['frequency'], "weekday")
            self.assertEqual(autoOff['time'], "19:00")

        create_configuration()
        update_configuration()

    def test3(self):
        print "\n---------------Combined Testcase 3---------------:"
        name = self.DO.getTimeStr("QATester_Combined_Testcase3_Create")
        print "Combined Step:"
        print "Step1: Create a configuration"
        print "Step2: filter by name in configurationList"
        print "Step3: Get ConfigurationDetail by ID"

        # Setp 1:
        def create_configuration():
            print "\n#### Setup 1: Create a configuration ####"
            query = """
mutation{
    createConfiguration(input:{name:"%s",
    description:"This is a unique configuration plan created by automation",
    unique:true}){
        configurationId
        name
        description
        createBy
        orgId
        createTime
        updateTime
        status
        appliedPanels
        failedInstalls
        }
}
                        """
            response = self.GQ.send_query(query % name, api='configuration')
            body = json.loads(response.text)
            self.global_var['id3'] = (body['data']['createConfiguration']['configurationId'])
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(body['data']['createConfiguration'])

        #  Setp 2:
        def configuration_list():
            print "\n#### Setup 2: Update Setup1 Created configuration ####"
            query = """
query{
configurationList(input:{pageNumber:1,pageSize:50,sortField:name,sortDirection:asc,
    filters:{name:"%s"}}){
            configurations{
                configurationId
                name
                description
                orgId
                createBy
                createTime
                updateTime
                appliedPanels
                failedInstalls
            }
            total
    }
}

                """

            response = self.GQ.send_query(query % name, api='configuration')
            body = json.loads(response.text)
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(body['data'])

        # Setp 3:
        def configuration_detail():
            print "\n#### Setup 3: Get Configuration Detail by ID####"
            query = """
query configurationDetail{
    configurationDetail(configurationId: "%s"){
        configurationId
        name
        description
        orgId
        createBy
        createTime
        updateTime
        appliedPanels
        failedInstalls
    }
}
"""
            response = self.GQ.send_query(query % self.global_var['id3'], api='configuration')
            body = json.loads(response.text)
            response_Id = body['data']['configurationDetail']['configurationId']
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response_Id, self.global_var['id3'])

        create_configuration()
        configuration_list()
        configuration_detail()

    def test4(self):

        print "\n---------------Combined Testcase 4---------------:"
        name = self.DO.getTimeStr("QATester_Combined_Testcase4_Create")
        print "Combined Step:"
        print "Step1: Create a configuration under parent ID:%s" % self.global_var['id2']
        print "Step2: filter by name in configurationList"
        print "Step3: Get Configuration Detail by Step1 CreateID"

        # Setp 1:
        def create_configuration():
            print "\n#### Setup 1: Create a configuration ####"
            query = """
mutation{
    createConfiguration(input:{name:"%s",
    description:"This is a unique configuration plan created by automation",
    unique:true, parent:"%s",configurationPayload:{
      autoOff:{
                frequency:"day"
                dayOfWeek:7
                time:"21:00"  
      }}}){
        configurationId
        name
        description
        createBy
        orgId
        createTime
        updateTime
        status
        appliedPanels
        failedInstalls
        }
}
                        """
            response = self.GQ.send_query(query % (name, self.global_var['id2']), api='configuration')
            body = json.loads(response.text)
            self.global_var['id4'] = (body['data']['createConfiguration']['configurationId'])
            self.assertEqual(response.status_code, 200)
            # self.assertIsNotNone(body['data']['createConfiguration'])

        #  Setp 2:
        def configuration_list():
            print "\n#### Setup 2: Get Setup1 Created configuration by Name ####"
            query = """
query{
configurationList(input:{pageNumber:1,pageSize:50,sortField:name,sortDirection:asc,
    filters:{name:"%s"}}){
            configurations{
                configurationId
                name
                description
                orgId
                createBy
                createTime
                updateTime
                appliedPanels
                failedInstalls
            }
            total
    }
}

                """

            response = self.GQ.send_query(query % name, api='configuration')
            body = json.loads(response.text)
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(body['data'])

        # Setp 3:
        def configuration_detail():
            print "\n#### Setup 3: Get Configuration Detail by ID####"
            query = """
query configurationDetail{
    configurationDetail(configurationId: "%s"){
        configurationId
        name
        description
        orgId
        createBy
        createTime
        updateTime
        appliedPanels
        failedInstalls
    }
}
"""
            response = self.GQ.send_query(query % self.global_var['id4'], api='configuration')
            body = json.loads(response.text)
            response_Id = body['data']['configurationDetail']['configurationId']
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response_Id, '%s' % self.global_var['id4'])

        create_configuration()
        configuration_list()
        configuration_detail()

    def test5(self):
        PanelSNList = []
        print "\n---------------Combined Testcase 5---------------:"
        name = self.DO.getTimeStr("QATester_Combined_Testcase4_Create")
        print "Combined Step:"
        print "Step1: Get 10 Panel SN"
        print "Step2: Deploy Configuration to Step1 SN List"
        print "Step3: Get Applied Panel by ID:%s" % self.global_var['id2']
        print "Step4: Get Deploy Config by First SN in PanelSNList"
        print "Step5: Show ActivityLogs"

        # Step 1:
        PanelList = self.DO.getRandomPanelSnAndNameList(3)
        print "\n#### Setup 1: Get PanelList: ####"
        for i in range(len(PanelList)):
            print PanelList[i]['serialNumber']
            PanelSNList.append(PanelList[i]['serialNumber'])
            self.global_var['SN%d' % (i+1)] = (PanelList[i]['serialNumber'])

        # Step 2:
        def deploy_configuration():
            print "\n#### Step2: Deploy Configuration to SN List by id %s ####" % self.global_var['id2']
            query = """
mutation{
    deployConfiguration(deployRequest:{
    serialNumbers:"%s",
    configurationId:"%s",
    isDelayed:true})}
                        """
            response = self.GQ.send_query(query % (PanelSNList, self.global_var['id2']), api='configuration')
            body = json.loads(response.text)
            # configurationId.append(body['data']['createConfiguration']['configurationId'])
            self.assertEqual(response.status_code, 200)
            # self.assertIsNotNone(body['data']['createConfiguration'])

        #  Step 3:
        def get_applied_panel():

            print "\n#### Setup 3: Get Applied Panel by ID:%s####" % self.global_var['id2']
            r, b = self.GQ.getAppliedPanel(self.global_var['id2'])
            self.assertEqual(r.status_code, 200)
            self.assertIsNotNone(b['data'])

        # Step 4:
        def get_deploy_config():
            print "\n#### Setup 4: Get Deploy Config by Panel SN:%s####" % self.global_var['SN1']
            r, b = self.GQ.getDeployConfig(self.global_var['SN1'])

            self.assertEqual(r.status_code, 200)

        # Step 5:
        def show_activity_logs():
            print "\n#### Setup 5: Show Activity Logs by Panel SN:%s####" % self.global_var['SN1']
            r, b = self.GQ.activityLogs(self.global_var['SN1'], 10, 0)
            self.assertEqual(r.status_code, 200)

        deploy_configuration()
        get_applied_panel()
        get_deploy_config()
        show_activity_logs()

    def test6(self):
        print "\n---------------Combined Testcase 6---------------:"
        name = self.DO.getTimeStr("QATester_Combined_Testcase4_Create")
        print "Combined Step:"
        print "Step1: Deploy Configuration:\n SN2:%s \n ID2:%s" % (self.global_var['SN2'], self.global_var['id2'])
        print "Step2: Deploy Configuration:\n SN2:%s \n ID1:%s" % (self.global_var['SN2'], self.global_var['id1'])
        print "Step3: Get Deploy Configuration by SN2:%s" % self.global_var['SN2']

        # Step 1:
        def deploy_configuration():
            print "\n#### Step2: Deploy Configuration to SN List by id %s ####" % self.global_var['id2']
            query = """
mutation{
    deployConfiguration(deployRequest:{
    serialNumbers:"%s",
    configurationId:"%s",
    isDelayed:true})}
                        """
            response = self.GQ.send_query(query % (self.global_var['SN2'], self.global_var['id2']), api='configuration')
            body = json.loads(response.text)
            # configurationId.append(body['data']['createConfiguration']['configurationId'])
            self.assertEqual(response.status_code, 200)
            # self.assertIsNotNone(body['data']['createConfiguration'])

        # Step 2:
        def deploy_configuration_id1():
            print "\n#### Step2: Deploy Configuration to SN List by id %s ####" % self.global_var['id1']
            query = """
    mutation{
        deployConfiguration(deployRequest:{
        serialNumbers:"%s",
        configurationId:"%s",
        isDelayed:true})}
                            """
            response = self.GQ.send_query(query % (self.global_var['SN2'], self.global_var['id1']),
                                          api='configuration')
            body = json.loads(response.text)
            # configurationId.append(body['data']['createConfiguration']['configurationId'])
            self.assertEqual(response.status_code, 200)
            # self.assertIsNotNone(body['data']['createConfiguration'])

        # Step 3:
        def get_deploy_config():
            print "\n#### Setup 4: Get Deploy Config by Panel SN:%s####" % self.global_var['SN2']
            r, b = self.GQ.getDeployConfig(self.global_var['SN2'])

            self.assertEqual(r.status_code, 200)

        deploy_configuration()
        deploy_configuration_id1()
        get_deploy_config()

    def test7(self):
        print "\n---------------Combined Testcase 7---------------:"
        name = self.DO.getTimeStr("QATester_Combined_Testcase7_Create")
        print "Combined Step:"
        print "Step1: Create a Configuration"
        print "Step2: Deploy Configuration SN3"
        print "Step3: Delete Configuration ID5"
        print 'Step4: Get Deploy Config SN3:%s' % self.global_var['SN3']

        # Setp 1:
        def create_configuration():
            name = self.DO.getTimeStr("QATester_Combined_Testcase7_Create")
            print "\n#### Setup 1: Create a configuration ####"
            query = """
mutation{
    createConfiguration(input:{name:"%s",
    description:"This is a unique configuration plan created by automation",
    unique:false, configurationPayload:{
    autoOff:{
    frequency:"day"
    dayOfWeek:7
    time:"21:00"  
    }}}){
        configurationId
        name
        description
        createBy
        orgId
        createTime
        updateTime
        status
        appliedPanels
        failedInstalls
        }
}
                                """
            response = self.GQ.send_query(query % name, api='configuration')
            body = json.loads(response.text)
            self.global_var['id5'] = (body['data']['createConfiguration']['configurationId'])
            self.assertEqual(response.status_code, 200)
            # self.assertIsNotNone(body['data']['createConfiguration'])

        # Step 2:
        def deploy_configuration_id1():
            print "Step2: Deploy Configuration:\n SN3:%s \n ID5:%s" % (self.global_var['SN3'], self.global_var['id5'])
            query = """
    mutation{
        deployConfiguration(deployRequest:{
        serialNumbers:"%s",
        configurationId:"%s",
        isDelayed:true})}
                            """
            response = self.GQ.send_query(query % (self.global_var['SN3'], self.global_var['id5']),
                                          api='configuration')
            body = json.loads(response.text)
            # configurationId.append(body['data']['createConfiguration']['configurationId'])
            self.assertEqual(response.status_code, 200)
            # self.assertIsNotNone(body['data']['createConfiguration'])

        # Step3:
        def delete_configuration():
            r, b = self.GQ.deleteConfiguration(self.global_var['id5'])
            self.assertEqual(r.status_code, 200)

        # Step 4:
        def get_deploy_config():
            print "\n#### Setup 4: Get Deploy Config by Panel SN3:%s####" % self.global_var['SN3']
            r, b = self.GQ.getDeployConfig(self.global_var['SN3'])

            self.assertEqual(r.status_code, 200)

        create_configuration()
        deploy_configuration_id1()
        delete_configuration()
        get_deploy_config()

    def test8(self):
        print "\n---------------Combined Testcase 8---------------:"
        name = self.DO.getTimeStr("QATester_Combined_Testcase8_Create")
        print "Combined Step:"
        print "Step1: Create a Configuration"
        print "Step2: Deploy Configuration SN3"
        print "Step3: Delete Configuration ID5"
        print "Step4: Get Deploy Config SN3:%s"
        print "Step5: Get Configuration Detail"

        # Setp 1:
        def create_configuration():
            name = self.DO.getTimeStr("QATester_Combined_Testcase8_Create")
            print "\n#### Setup 1: Create a configuration ####"
            query = """
mutation{
    createConfiguration(input:{name:"%s",
    description:"This is a unique configuration plan created by automation",
    unique:false, configurationPayload:{
    autoOff:{
    frequency:"day"
    dayOfWeek:7
    time:"21:00"  
    }}}){
        configurationId
        name
        description
        createBy
        orgId
        createTime
        updateTime
        status
        appliedPanels
        failedInstalls
        }
}
                                """
            response = self.GQ.send_query(query % name, api='configuration')
            body = json.loads(response.text)
            self.global_var['id6'] = (body['data']['createConfiguration']['configurationId'])
            self.assertEqual(response.status_code, 200)
            # self.assertIsNotNone(body['data']['createConfiguration'])

        # Step 2:
        def deploy_configuration_id1():
            print "Step2: Deploy Configuration:\n SN3:%s \n ID5:%s" % (self.global_var['SN3'], self.global_var['id6'])
            query = """
    mutation{
        deployConfiguration(deployRequest:{
        serialNumbers:"%s",
        configurationId:"%s",
        isDelayed:true})}
                            """
            response = self.GQ.send_query(query % (self.global_var['SN3'], self.global_var['id6']),
                                          api='configuration')
            body = json.loads(response.text)
            # configurationId.append(body['data']['createConfiguration']['configurationId'])
            self.assertEqual(response.status_code, 200)
            # self.assertIsNotNone(body['data']['createConfiguration'])

        # Step3:
        def delete_configuration():
            r, b = self.GQ.deleteConfiguration(self.global_var['id5'])
            self.assertEqual(r.status_code, 200)

        # Step 4:
        def get_deploy_config():
            print "\n#### Setup 4: Get Deploy Config by Panel SN3:%s####" % self.global_var['SN3']
            r, b = self.GQ.getDeployConfig(self.global_var['SN3'])

            self.assertEqual(r.status_code, 200)

        # Setp 5:
        def configuration_detail():
            print "\n#### Setup 5: Get Configuration Detail by ID %s####" % self.global_var['id6']
            query = """
    query configurationDetail{
        configurationDetail(configurationId: "%s"){
            configurationId
            name
            description
            orgId
            createBy
            createTime
            updateTime
            appliedPanels
            failedInstalls
        }
    }
    """
            response = self.GQ.send_query(query % self.global_var['id6'], api='configuration')
            body = json.loads(response.text)
            self.assertEqual(response.status_code, 200)
            self.assertIsNone(body['data']['configurationDetail'])

        create_configuration()
        deploy_configuration_id1()
        delete_configuration()
        get_deploy_config()
        configuration_detail()


if __name__ == '__main__':
    unittest.main()
