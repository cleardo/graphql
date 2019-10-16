# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
import json
from config import prome_config as con


class CreateConfiguration(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_create_configuration(self):

        times = 6
        description = "QATester_create_configuration"

        def create_configuration(i, name, description):
            print "############# Testing %d  Create Configuration #############" % (i + 1)
            print "Crate configuration name is ", name
            r, b = self.GQ.createConfiguration(name, description)

            # --------------------断言 assert--------------------
            # 断言API正在运行  assertEqual API server is running
            self.assertEqual(r.status_code, 200)

        for i in range(times):
            name = self.DO.getTimeStr("QATester_create_configuration") + str(i)
            create_configuration(i, name, description)

    def test_configurationId_name_is_existed(self):
        lsitr, listb = self.GQ.configurationList(1, 1, showprint=False)
        name = listb['data']['configurationList']['configurations'][0]['name']
        print "#### Test  configuration name is existed ####"
        query = """
mutation{
  createConfiguration(input:{name:"%s",
    description:""})
  {
    configurationId,
    name,
    description,
  }
}
    """
        r = self.GQ.send_query(query % name, api='configuration')
        b = json.loads(r.text)
        self.assertEqual(b['data']['createConfiguration'], None)
        self.assertIsNotNone(b['errors'])
        self.assertEqual(r.status_code, 200)

        def description_is_123():
            print "#### Test  configuration name is existed ####"
            query = """
mutation{
  createConfiguration(input:{name:"%s",
    description:"123"})
  {
    configurationId,
    name,
    description,
  }
}
                """
            r = self.GQ.send_query(query % name, api='configuration')
            b = json.loads(r.text)
            self.assertEqual(b['data']['createConfiguration'], None)
            self.assertIsNotNone(b['errors'])
            self.assertEqual(r.status_code, 200)

        description_is_123()



if __name__ == '__main__':
    unittest.main()
