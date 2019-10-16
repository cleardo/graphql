# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
import json
from config import prome_config as con


class ConfigurationList(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_configurationList(self):

        times = 1
        pageNumber = 1
        pageSize = 1

        def configurationList(i, pageNumber, pageSize):
            print "#################### Testing %d  configurationList ####################" % (i + 1)
            r, b = self.GQ.configurationList(pageNumber, pageSize)

            # --------------------断言 assert--------------------
            # 断言API正在运行  assertEqual API server is running
            self.assertEqual(r.status_code, 200)

        for i in range(times):
            configurationList(i, pageNumber, pageSize)

    def test_pagenumber_2(self):
        print "#### Test pagenumber more than 1,inputpageSize more than 1 ####"
        query = """
query{
  configurationList(input:{pageNumber:2,pageSize:2,sortField:name,sortDirection:asc,
    filters:{name:""}})
  {
    configurations{
      configurationId,
      name,
      description,
      orgId,
      createBy,
      createTime,
      updateTime,
      appliedPanels,
      failedInstalls,
    },
   total
  }
}
                                                    """
        r = self.GQ.send_query(query, api='configuration')
        b = json.loads(r.text)
        self.assertIsNotNone(b['data'])
        self.assertEqual(r.status_code, 200)

    def test_inputpageSize_is0(self):
            print "#### Test pagenumber more than 1,inputpageSize is 0 ####"
            query = """
query{
  configurationList(input:{pageNumber:2,pageSize:0,sortField:name,sortDirection:asc,
    filters:{name:""}})
  {
    configurations{
      configurationId,
      name,
      description,
      orgId,
      createBy,
      createTime,
      updateTime,
      appliedPanels,
      failedInstalls,
    },
   total
  }
}
                                                        """
            r = self.GQ.send_query(query, api='configuration')
            b = json.loads(r.text)
            self.assertIsNotNone(b['data'])
            self.assertEqual(r.status_code, 200)

    def test_inputpageSize_is_plural_1(self):
        print "#### Test pagenumber more than 1,inputpageSize is -1 ####"
        query = """
query{
  configurationList(input:{pageNumber:2,pageSize:-1,sortField:name,sortDirection:asc,
    filters:{name:""}})
  {
    configurations{
      configurationId,
      name,
      description,
      orgId,
      createBy,
      createTime,
      updateTime,
      appliedPanels,
      failedInstalls,
    },
   total
  }
}
                                                            """
        r = self.GQ.send_query(query, api='configuration')
        b = json.loads(r.text)
        self.assertIsNotNone(b['data'])
        self.assertEqual(r.status_code, 200)

    def test_inputpageSize_is_plural_2(self):
            print "#### Test pagenumber more than 1,inputpageSize is -2 ####"
            query = """
query{
  configurationList(input:{pageNumber:2,pageSize:-2,sortField:name,sortDirection:asc,
    filters:{name:""}})
  {
    configurations{
      configurationId,
      name,
      description,
      orgId,
      createBy,
      createTime,
      updateTime,
      appliedPanels,
      failedInstalls,
    },
   total
  }
}
                                                                """
            r = self.GQ.send_query(query, api='configuration')
            b = json.loads(r.text)
            self.assertIsNotNone(b['data'])
            self.assertEqual(r.status_code, 200)

    def test_filters_name_is_empty(self):
        print "#### Test filters name is empty ####"
        query = """
query{
  configurationList(input:{pageNumber:2,pageSize:2,sortField:name,sortDirection:asc,
    filters:{name:""}})
  {
    configurations{
      configurationId,
      name,
      description,
      orgId,
      createBy,
      createTime,
      updateTime,
      appliedPanels,
      failedInstalls,
    },
   total
  }
}
                                                                    """
        r = self.GQ.send_query(query, api='configuration')
        b = json.loads(r.text)
        self.assertIsNotNone(b['data'])
        self.assertEqual(r.status_code, 200)

    def test_filters_name_is_true(self):
        print "#### Test filters name is is existed ####"
        query = """
query{
  configurationList(input:{pageNumber:2,pageSize:2,sortField:name,sortDirection:asc,
    filters:{name:"$1"}})
  {
    configurations{
      configurationId,
      name,
      description,
      orgId,
      createBy,
      createTime,
      updateTime,
      appliedPanels,
      failedInstalls,
    },
   total
  }
}
"""
        r = self.GQ.send_query(query, api='configuration')
        b = json.loads(r.text)
        self.assertIsNotNone(b['data'])
        self.assertEqual(r.status_code, 200)

    def test_configurationId_is_empty(self):
        print "#### Test configurationId is empty ####"
        query = """
query{
  configurationDetail(configurationId:"")
  {
      configurationId,
      name,
      description,
      orgId,
      createBy,
      createTime,
      updateTime,
      appliedPanels,
      failedInstalls,
      status,
      unique,
      configurationPayload,
  }
}
"""
        r = self.GQ.send_query(query, api='configuration')
        b = json.loads(r.text)
        self.assertEqual(b['data']['configurationDetail'], None)
        self.assertEqual(r.status_code, 200)

    def test_configurationId_is_error(self):
        print "#### Test configurationId is wrong ####"
        query = """
query{
  configurationDetail(configurationId:"$1!!!!!!!!!!!!@@@!!!!!@@!@!@!@")
  {
      configurationId,
      name,
      description,
      orgId,
      createBy,
      createTime,
      updateTime,
      appliedPanels,
      failedInstalls,
      status,
      unique,
      configurationPayload,
  }
}
"""
        r = self.GQ.send_query(query, api='configuration')
        b = json.loads(r.text)
        self.assertEqual(b['data']['configurationDetail'], None)
        self.assertIsNotNone(b['errors'])
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
