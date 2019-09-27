# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
import time
from config import prome_config as con

class CreateTag(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_create_tag(self):

        if con.AutoTestMode and con.AutoTestMode is False:

            if con.test_create_tag_times and len(con.test_create_tag_times) != 0:
                times = con.test_create_tag_times
            else:
                times = 1

            if con.test_create_tag_tagname and len(con.test_create_tag_tagname) != 0 and \
                    con.test_create_tag_tagGroup and len(con.test_create_tag_tagGroup):
                tagname = con.test_create_tag_tagname
                tagGroup = con.test_create_tag_tagGroup
            else:
                tagname = self.DO.getTimeStr("QATest_create_tag") + str(i + 1)
                tagGroup = "Not in AutoTest mode"
        else:
            tagGroup = "QAtester-CreateTag"
            times = 6

        def create_tag(i, tagname, tagGroup):
            print "####################Testing %d Create Tag####################" % (i+1)
            print '\ncreate tag name  is :', tagname
            print '\nadd tag group is :', tagGroup
            response, body = self.GQ.createTag(tagGroup, tagname)
            # --------------------断言 assert--------------------
            # 断言 API正在运行  assertEqual API server is running
            self.assertEqual(response.status_code, 200)
            # 断言 创建tag 成功
            self.assertEqual(body['data']['createTag']['group'], tagGroup)
            self.assertEqual(body['data']['createTag']['value'], tagname)

        for i in range(times):
            if con.AutoTestMode and con.AutoTestMode is False:
                create_tag(i, tagname, tagGroup)
            else:
                tagname = self.DO.getTimeStr("QATest_create_tag") + str(i)
                create_tag(i, tagname, tagGroup)
