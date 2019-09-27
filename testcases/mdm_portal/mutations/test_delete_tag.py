# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
from config import prome_config as con
import unittest


class DeleteTag(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_delete_tag(self):
        if con.AutoTestMode and con.AutoTestMode is False:
            if con.test_delete_tag_times and len(con.test_delete_tag_times):
                times = con.test_delete_tag_times
            else:
                times = 1

            if con.test_delete_tag_tagidList and len(test_delete_tag_tagidList) != 0:
                if test_delete_tag_group and len(test_delete_tag_group) == 0:
                    tagidList = con.test_delete_tag_tagidList
                    NoEnterGroup = True
                else:
                    tagGroup = test_delete_tag_group
                    tagList = self.DO.getTagListByGroupName(tagGroup)
            else:
                tagGroup = test_delete_tag_group
                tagList = self.DO.getTagListByGroupName(tagGroup)

        else:
            times = 1
            group = "QAtester-CreateTag"
            tagList = self.DO.getTagListByGroupName(group)

        def delete_tag(i, tagid):
            print "####################Testing %d Delete Tag####################" % (i + 1)
            print '\ndelete tagid is :', tagid
            response, body = self.GQ.deleteTag(tagid)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(body['data']['deleteTag']['id'], tagid)

        for i in range(times):
            # 指定参数模式
            if con.AutoTestMode and con.AutoTestMode is False:
                if NoEnterGroup is True:
                    for j in range(len(tagidList)):
                        tagid = tagidList[j]['tagid']
                        delete_tag(i, tagid)
                else:
                    for j in range(len(tagList)):
                        tagid = tagList[j]['tagid']
                        delete_tag(i, tagid)
            # 自动模式
            else:
                tagid = tagList[i]['tagid']
                delete_tag(i, tagid)
